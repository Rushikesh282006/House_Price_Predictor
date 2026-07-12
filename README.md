# House Price Prediction API

A FastAPI app that predicts California house prices using a trained `RandomForestRegressor` model.

## Project overview

This project demonstrates a complete machine learning deployment workflow. It trains a regression model on the California Housing dataset, saves the trained model as a serialized artifact, and exposes prediction endpoints through a FastAPI web service.

## Data and model

- Dataset: `sklearn.datasets.fetch_california_housing`
- Model: `sklearn.ensemble.RandomForestRegressor`
- Serialization: `joblib`
- Endpoints: single JSON prediction and batch CSV upload prediction

## What this project contains

- `main.py` — FastAPI app with two prediction endpoints
- `train.py` — script that trains the model and saves the required `.joblib` files
- `test_file.csv` — example CSV input for batch prediction
- `requirements.txt` — Python dependencies
- `.gitignore` — files to ignore for GitHub
- `README.md` — this documentation

## Model evaluation

The training script prints model performance metrics such as mean absolute error and R² score. These outputs provide a quick sanity check on model quality before deploying the API.

## Important note about model files

The trained files `house_price_predictor.joblib` and `house_features.joblib` may be large and should not be committed if GitHub rejects them.

If you clone the repo and the model files are not present, run:

```powershell
python train.py
```

That command creates both required files locally.

## Setup instructions

1. Open PowerShell in the project folder.

```powershell
cd path\to\project\folder
```

2. Create a virtual environment:

```powershell
python -m venv venv
```

3. Activate the virtual environment:

```powershell
.\venv\Scripts\Activate.ps1
```

4. Install Python dependencies:

```powershell
python -m pip install -r requirements.txt
```

5. Create the model files if they do not exist:

```powershell
python train.py
```

## Run the API server

```powershell
python -m uvicorn main:app --reload
```

Then open the browser at:

```text
http://127.0.0.1:8000/docs
```

## API endpoints

This project supports both interactive and programmatic access. You can test the API directly from the Swagger UI at `/docs` or by sending requests from any HTTP client.

### `GET /`
Returns a basic health message.

### `GET /health`
Returns model status and average error information.

### `POST /predict`
Use this endpoint to send a single house feature set as JSON.

Example request body:

```json
{
  "MedInc": 5.0,
  "HouseAge": 30.0,
  "AveRooms": 6.0,
  "AveBedrms": 1.0,
  "Population": 1500.0,
  "AveOccup": 3.0,
  "Latitude": 37.0,
  "Longitude": -121.0
}
```

### `POST /predict-file`
Use this endpoint to upload a CSV file with many rows for batch prediction.

The CSV file must include these columns:

- `MedInc`
- `HouseAge`
- `AveRooms`
- `AveBedrms`
- `Population`
- `AveOccup`
- `Latitude`
- `Longitude`

Example CSV file: `test_file.csv`

## How to use the app after cloning

1. Install dependencies.
2. Run `python train.py` if model files are missing.
3. Start the server with `python -m uvicorn main:app --reload`.
4. Test the API at `http://127.0.0.1:8000/docs`.
