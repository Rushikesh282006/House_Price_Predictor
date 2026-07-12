# House Price Prediction API

This repository contains a FastAPI app for predicting California house prices using a trained RandomForest model.

## Files to include in GitHub

- `main.py` — FastAPI application with `/predict` and `/predict-file` endpoints
- `train.py` — script to train the model and save `house_price_predictor.joblib`
- `test_file.csv` — sample CSV input for batch prediction
- `README.md` — project documentation
- `.gitignore` — files and folders to ignore
- `requirements.txt` — Python dependencies

### Optional

- `house_price_predictor.joblib` — trained model artifact
- `house_features.joblib` — saved feature list

If you do not want to include binary model files in GitHub, the reader can generate them by running `python train.py`.

## What to ignore

The repository should ignore:

- `venv/` directory
- `__pycache__/` Python caches
- `prediction.csv` generated output
- `.env` or other local environment files

## Setup

1. Create a Python virtual environment:

```bash
python -m venv venv
```

2. Activate the environment:

- Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

- Windows CMD:

```cmd
venv\Scripts\activate.bat
```

3. Install dependencies:

```bash
python -m pip install -r requirements.txt
```

4. Train the model (if needed):

```bash
python train.py
```

## Run the API

```bash
python -m uvicorn main:app --reload
```

Open `http://127.0.0.1:8000/docs` to test the API.

## Endpoints

- `GET /` — health message
- `GET /health` — model status
- `POST /predict` — single prediction via JSON body
- `POST /predict-file` — upload CSV file for batch prediction

## CSV upload format

The CSV must include these headers:

- `MedInc`
- `HouseAge`
- `AveRooms`
- `AveBedrms`
- `Population`
- `AveOccup`
- `Latitude`
- `Longitude`

Example `test_file.csv` is already provided.
