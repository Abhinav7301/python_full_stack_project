#api/main.py
from fastapi import FASTAPI , HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import sys,os

#import Taskmanager from src
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.logic import TaskManager

#-----------------------------App Setup-----------------------------

app = FASTAPI(title="Weather Data Analyzer", version="1.0")

# ---------------------------------Allow Frontend(streamlit/React) ro call the API---------------

app.add_middleware(
    CORSMiddleware,
    allow_origin=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
#---------------------------------Data Model-----------------------------
class WeatherData(BaseModel):
    day: str
    temperature: float
    category: str
class UpdateWeatherData(BaseModel):
    day: str | None = None
    temperature: float | None = None
    category: str | None = None
class DeleteResponse(BaseModel):
    message: str
class ErrorResponse(BaseModel):
    error: str
#---------------------------------API Endpoints-----------------------------
task_manager = TaskManager()
@app.post("/weather", response_model=dict)
def create_weather_data(data: WeatherData):
    result = task_manager.create_task(data.day, data.temperature, data.category)
    if "error" in result:
        raise HTTPException(status_code=400, detail=result["error"])
    return result
@app.get("/weather", response_model=list[dict])
def get_weather_data():
    return task_manager.get_tasks()
@app.put("/weather/{record_id}", response_model=dict, responses={400: {"model": ErrorResponse}})
def update_weather_data(record_id: int, data: UpdateWeatherData):
    result = task_manager.update_task(record_id, data.day, data.temperature, data.category)
    if "error" in result:
        raise HTTPException(status_code=400, detail=result["error"])
    return result
@app.delete("/weather/{record_id}", response_model=DeleteResponse, responses={400: {"model": ErrorResponse}})
def delete_weather_data(record_id: int):
    result = task_manager.delete_task(record_id)
    if "error" in result:
        raise HTTPException(status_code=400, detail=result["error"])
    return result
#---------------------------------Run the app-----------------------------
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="", port=8000)
#         query = f"UPDATE WeatherData SET {', '.join(fields)} WHERE id = ?"
#         conn.execute(query, values)
#         conn.commit()
#         return {"message": "Record updated successfully"}



            




