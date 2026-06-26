
================================================================================
MEDICINE IMAGE CLASSIFICATION - OUTPUT PACKAGE
================================================================================
Generated: 2026-03-31 22:00:48
Test Accuracy: 88.80114860014358%
Total Epochs: 70
================================================================================

FOLDER STRUCTURE:
-----------------
01_Visualizations/     - All training curves, confusion matrix, sample predictions
   ├── visualizations/ - 20+ PNG files showing model performance

02_Reports/            - JSON and TXT reports with detailed metrics
   ├── reports/        - dataset_statistics.json, final_report.json, etc.

03_Models/             - Trained model in multiple formats
   ├── models/         - final_model.keras, final_model.h5, tfjs_model/

04_Checkpoints/        - Best models from each training phase
   ├── checkpoints/    - best_model_phase1.keras, best_model_phase2.keras, etc.

05_Configurations/     - Configuration files
   └── config.json     - Training configuration

00_README_FIRST.json   - This summary file

================================================================================
KEY METRICS:
================================================================================
- Test Accuracy: 88.80%
- Macro F1 Score: 0.8701
- Weighted F1 Score: 0.8870
- Total Images: 13,955
- Classes: 20
- Training Epochs: 70 (Phase1:20, Phase2:30, Phase3:20)

================================================================================
USAGE NOTES:
================================================================================
1. To load the model in Python:
   from tensorflow.keras.models import load_model
   model = load_model('03_Models/models/final_model.keras')

2. For browser inference, use the TF.js model in:
   03_Models/models/tfjs_model/

3. Class mapping is available in:
   02_Reports/reports/dataset_statistics.json (under 'classes')

================================================================================
