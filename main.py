import joblib as jb
import pandas as pd
from fastapi import FastAPI,HTTPException,UploadFile,File
from pydantic import BaseModel,Field
import io
from fastapi.responses import StreamingResponse


app = FastAPI()

model = jb.load("house_price_predictor.joblib")
features = jb.load("house_features.joblib")
avg_error = 32800
#input 
class Model_Input(BaseModel):
    MedInc : float = Field(gt=0,le=55,description="Median Income of Neighbourhood")
    HouseAge : float = Field(gt=0,le=100,description="Age of house")
    AveRooms : float = Field(gt=0,description="No. of rooms")
    AveBedrms : float = Field(gt=0,description="No. of Bedrooms")
    Population : float = Field(gt=0,le=10000,description="Total Population")
    AveOccup : float = Field(gt=0, description="Average no. of people living in one house")
    Latitude : float = Field(gt=31, le=42,description="Latitude of house")
    Longitude : float = Field(gt=-125, le=-114,description="Longitude of house")

@app.get("/")
def home():
    return {
        "message" : "California house prediction api",
        "status" : "running",
        "endpoint" : "send POST request to /predict"
        }

@app.get('/health')
def health():
    return{
        "status" : "running",
        "model" : "RandomForestRegressor",
        "avg_error" : f"${avg_error}"
    }


@app.post("/predict")
def predict(house:Model_Input):
    try:
        input_data = pd.DataFrame([{
        "MedInc" : house.MedInc,
        "HouseAge" : house.HouseAge,
        "AveRooms" : house.AveRooms,
        "AveBedrms" : house.AveBedrms,
        "Population" : house.Population,
        "AveOccup" : house.AveOccup,
        "Latitude" : house.Latitude,
        "Longitude" : house.Longitude
        }])

        predicted_price = model.predict(input_data)[0]
        price_usd = predicted_price * 100000
        return {
            "predicted_price" : f"${price_usd:,.0f}",
            "confidence_range" : f"${price_usd-avg_error:,.0f} to ${price_usd+avg_error:,.0f}"
        }
    
    except Exception as e:
        print("Prediction error:", e)
        raise HTTPException(
            status_code = 500,
            detail = f"prediction failed: {e}"
        )
    
@app.post('/predict-file')
async def predFile(file:UploadFile=File(...)):
    if not file.filename.endswith('.csv'):
        raise HTTPException(
            status_code=400,
            detail="Please Upload a 'CSV' file"
        )
    contents = await file.read()
    df = pd.read_csv(io.BytesIO(contents))

    required_cols = ["MedInc","HouseAge","AveRooms","AveBedrms","Population","AveOccup","Latitude","Longitude"]

    missing_cols = [col for col in required_cols if col not in df.columns]

    if missing_cols:
        raise HTTPException(
            status_code=400,
            detail=f"The following columns are missing from file {missing_cols}"
        )

    if len(df) == 0 :
        raise HTTPException(
            status_code=400,
            detail="The uploaded file is empty"
        )
    
    try:
        predictions = model.predict(df[required_cols])
        prices_usd = [pred * 100000 for pred in predictions]
        df["predicted_price_usd"] = [f"${x:,.0f}" for x in prices_usd]
        output = df.to_csv(index=False)

        return StreamingResponse(
            io.StringIO(output),
            media_type="text/csv",
            headers={
                "Content-Disposition":"attachment; filename=prediction.csv"
            }
        )

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Prediction failed:{str(e)}"
        )