# app.py - Standalone Medicine Recognition API
# Run from this folder with: python app.py
# For the full web interface, please use the provided Jupyter notebook.

import os
import sqlite3
import json
from flask import Flask, request, jsonify
from flask_cors import CORS
from PIL import Image
import numpy as np
import tensorflow as tf

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Load model, labels, and local medicine database from the organized output package.
MODEL_PATH = os.path.join(BASE_DIR, '03_Models', 'models', 'final_model.keras')
LABELS_PATH = os.path.join(BASE_DIR, 'class_labels.json')
DB_PATH = os.path.join(BASE_DIR, 'medicine_app.db')

model = tf.keras.models.load_model(MODEL_PATH)
with open(LABELS_PATH, 'r') as f:
    class_labels = json.load(f)['class_names']

NDC_TO_NAME = {
    '00378-0208': 'Pioglitazone', '00378-3855': 'Metformin',
    '00591-0461': 'Tramadol', '16729-0020': 'Escitalopram',
    '16729-0168': 'Allopurinol', '50111-0434': 'Primidone',
    '53489-0156': 'Quetiapine', '53746-0544': 'Levetiracetam',
    '57664-0377': 'Ranitidine', '62037-0831': 'Metoprolol Succinate',
    '62037-0832': 'Metoprolol Tartrate', '64380-0803': 'Divalproex',
    '65162-0253': 'Oxcarbazepine', '67253-0901': 'Doxazosin',
    '68382-0008': 'Naproxen', '68382-0227': 'Hydroxychloroquine',
    '69097-0127': 'Carvedilol', '69097-0128': 'Carvedilol Phosphate',
    '69315-0904': 'Venlafaxine', '69315-0905': 'Venlafaxine XR',
}

def predict_medicine(image_bytes):
    img = Image.open(image_bytes).convert('RGB')
    img = img.resize((224, 224))
    img_array = np.array(img, dtype=np.float32) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    probs = model.predict(img_array, verbose=0)[0]
    top_idx = np.argmax(probs)
    confidence = float(probs[top_idx])
    ndc = class_labels[top_idx]
    status = 'HIGH_CONFIDENCE' if confidence >= 0.8 else 'LOW_CONFIDENCE' if confidence >= 0.5 else 'UNKNOWN'
    return {
        'ndc_code': ndc,
        'generic_name': NDC_TO_NAME.get(ndc, ndc),
        'confidence': confidence,
        'confidence_percent': f"{confidence*100:.1f}%",
        'status': status
    }

def fetch_medicine_details(ndc):
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM medicines WHERE id = ?", (ndc,))
    row = cursor.fetchone()
    conn.close()
    return dict(row) if row else None

def check_interaction(ndc1, ndc2):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        SELECT severity, description, recommendation
        FROM drug_interactions
        WHERE (drug1_id = ? AND drug2_id = ?) OR (drug1_id = ? AND drug2_id = ?)
        LIMIT 1
    """, (ndc1, ndc2, ndc2, ndc1))
    row = cursor.fetchone()
    conn.close()
    if row:
        return {'severity': row[0], 'description': row[1], 'recommendation': row[2]}
    return {'severity': 'None', 'description': 'No known interaction.', 'recommendation': 'Consult a doctor.'}

app = Flask(__name__)
CORS(app)

@app.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return jsonify({'error': 'No image'}), 400
    file = request.files['image']
    img_bytes = file.read()
    result = predict_medicine(img_bytes)
    if result['status'] != 'UNKNOWN':
        details = fetch_medicine_details(result['ndc_code'])
        if details:
            result['medicine_details'] = details
    return jsonify(result)

@app.route('/interaction', methods=['POST'])
def interaction():
    data = request.get_json()
    return jsonify(check_interaction(data.get('ndc1'), data.get('ndc2')))

@app.route('/medicines', methods=['GET'])
def get_medicines():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT id, generic_name, brand_name FROM medicines")
    meds = [{'id': r[0], 'generic_name': r[1], 'brand_name': r[2]} for r in cursor.fetchall()]
    conn.close()
    return jsonify({'medicines': meds})

@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'ok', 'model_loaded': True})

if __name__ == '__main__':
    print("Starting MediScan server at http://localhost:5000")
    print("Note: For the full web interface, please use the Jupyter notebook.")
    app.run(host='0.0.0.0', port=5000, debug=False)
