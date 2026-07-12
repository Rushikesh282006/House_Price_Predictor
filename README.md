# House Price Prediction API

A FastAPI app that predicts California house prices using a trained RandomForest model.

## What this project contains

- `main.py` — FastAPI app with two prediction endpoints
- `train.py` — script that trains the model and saves the required `.joblib` files
- `test_file.csv` — example CSV input for batch prediction
- `requirements.txt` — Python dependencies
- `.gitignore` — files to ignore for GitHub
- `README.md` — this documentation


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
