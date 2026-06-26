SMART MEDICINE RECOGNITION SYSTEM — Phase 3
============================================

HOW TO RUN LOCALLY:
Step 1: Install requirements
        pip install flask flask-cors tensorflow pillow

Step 2: Place these files in the same folder:
        - app.py
        - final_model.keras
        - medicine_app.db
        - class_labels.json

Step 3: Run the application
        python app.py

Step 4: Open your browser
        http://localhost:5000

HOW TO RUN ON GOOGLE COLAB:
Step 1: Open Medicine_WebApp_Phase3.ipynb in Colab
Step 2: Run all cells from top to bottom
Step 3: Cell 5 will print a public ngrok URL
Step 4: Open that URL in your browser

REQUIREMENTS:
Python 3.8+, TensorFlow 2.x, Flask, flask-cors, Pillow

NOTE: final_model.keras must be present.
Download from Google Drive if needed.
