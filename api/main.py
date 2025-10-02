# api/main.py
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import sys, os

# Import TaskManager from src
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.logic import TaskManager

# ----------------------------- App Setup -----------------------------
app = FastAPI(title="Weather Data Analyzer", version="1.0", debug=True)

# Allow Frontend (Streamlit/React) to call the API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # allow all origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ----------------------------- Data Models -----------------------------
class WeatherData(BaseModel):
    day: str
    temperature: float

class UpdateWeatherData(BaseModel):
    day: str | None = None
    temperature: float | None = None
    category: str | None = None

class DeleteResponse(BaseModel):
    message: str

class ErrorResponse(BaseModel):
    error: str

# ----------------------------- API Endpoints -----------------------------
task_manager = TaskManager()

# CREATE
@app.post("/weather", response_model=dict, responses={400: {"model": ErrorResponse}})
def create_weather_data(data: WeatherData):
    result = task_manager.create_record(data.day, data.temperature)
    if "error" in result:
        raise HTTPException(status_code=400, detail=result["error"])
    return result

# READ
@app.get("/weather", response_model=dict)
def get_weather_data():
    return task_manager.read_records()

# UPDATE
@app.put("/weather/{record_id}", response_model=dict, responses={400: {"model": ErrorResponse}})
def update_weather_data(record_id: int, data: UpdateWeatherData):
    result = task_manager.update_record(record_id, data.day, data.temperature, data.category)
    if "error" in result:
        raise HTTPException(status_code=400, detail=result["error"])
    return result

# DELETE
@app.delete("/weather/{record_id}", response_model=DeleteResponse, responses={400: {"model": ErrorResponse}})
def delete_weather_data(record_id: int):
    result = task_manager.delete_record(record_id)
    if "error" in result:
        raise HTTPException(status_code=400, detail=result["error"])
    return result

# ----------------------------- Run the app -----------------------------
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
