import os
import gdown
import joblib

MODEL_PATH = "predictor/models/random_forest_model.joblib"
SCALER_PATH = "predictor/models/scaler.joblib"

def load_files():
    os.makedirs("predictor/models", exist_ok=True)

    if not os.path.exists(MODEL_PATH):
        print("Downloading model...")
        gdown.download(
            "https://drive.google.com/uc?id=1Ex8t-O4verZN7z1BLNKUpuSs3vL_nZng",
            MODEL_PATH,
            quiet=False
        )

    if not os.path.exists(SCALER_PATH):
        print("Downloading scaler...")
        gdown.download(
            "https://drive.google.com/uc?id=1gpgKpUpqDzFSmTNgFUCmq7-CZAHbLodR",
            SCALER_PATH,
            quiet=False
        )

    model = joblib.load(MODEL_PATH)
    scaler = joblib.load(SCALER_PATH)

    return model, scaler