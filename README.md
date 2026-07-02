# Smart Medicine Recognition Application

Instant pill identification and safety guidance from a medicine image scan.

This repository contains the training notebooks, trained model artifacts, Flask API, reports, and visualizations for a Smart Medicine Recognition final year project. The system predicts the medicine/NDC class from an uploaded pill image and provides supporting medicine details and interaction checks through a local SQLite database.

## Features

- Medicine image classification using a trained TensorFlow/Keras model.
- Flask API for prediction, medicine listing, health check, and interaction lookup.
- Training and evaluation notebooks for all project phases.
- Model outputs, checkpoints, training reports, and visualizations.
- Dataset notes kept separately because raw dataset archives are too large for normal GitHub storage.

## Project Structure:

```text
Smart-Medicine-Recognition-Application/
|-- README.md
|-- .gitignore
|-- requirements.txt
|-- datasets/
|   `-- README.md
|-- notebooks/
|   |-- phase_1_2_training.ipynb
|   `-- phase_3_to_6_app_evaluation.ipynb
`-- medicine_output/
    |-- app.py
    |-- class_labels.json
    |-- medicine_app.db
    |-- APP_RUN_README.txt
    |-- OUTPUT_PACKAGE_README.txt
    |-- 00_README_FIRST.json
    |-- 01_Visualizations/
    |   `-- visualizations/
    |-- 02_Reports/
    |   `-- reports/
    |-- 03_Models/
    |   `-- models/
    |       |-- final_model.keras
    |       |-- final_model.h5
    |       |-- class_labels.json
    |       `-- tfjs_model/
    |-- 04_Checkpoints/
    |   `-- checkpoints/
    `-- 05_Configurations/
        `-- config.json
```

## Model Summary

- Test accuracy: 88.80%
- Macro F1 score: 0.8701
- Weighted F1 score: 0.8870
- Total images used in training/evaluation: 13,955
- Classes: 20 medicine/NDC classes
- Training epochs: 70 across three training phases

## Setup

Use Python 3.8 or newer.

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

On macOS/Linux, activate the environment with:

```bash
source .venv/bin/activate
```

## Run The Flask API

```bash
cd medicine_output
python app.py
```

The API starts at:

```text
http://localhost:5000
```

Useful endpoints:

- `GET /health` - check server/model status.
- `GET /medicines` - list medicines from the local database.
- `POST /predict` - upload an image using form-data key `image`.
- `POST /interaction` - send JSON with `ndc1` and `ndc2`.

## Notebooks

- `notebooks/phase_1_2_training.ipynb` contains the early dataset preparation and training phases.
- `notebooks/phase_3_to_6_app_evaluation.ipynb` contains later evaluation, export, and application work.

## Datasets

Large raw dataset archives are not tracked in Git because several files exceed GitHub's normal file-size limit. Keep the dataset zip files locally or use Git LFS/cloud storage for sharing them.

Expected local dataset archive names are documented in `datasets/README.md`.

## Important Notes

- The trained models and checkpoints are included under `medicine_output/03_Models/` and `medicine_output/04_Checkpoints/`.
- Future raw datasets, database dumps, and model binaries are ignored by `.gitignore` to avoid accidental oversized commits.
- This project is for academic/demo use. Medicine identification and safety guidance should always be verified by a qualified healthcare professional.
