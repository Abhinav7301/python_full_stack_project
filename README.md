# Weather Data Analysis

## Description

This project is about **analyzing a week’s temperature data**.  
It stores daily temperature readings, calculates basic statistics, and classifies days into **Hot**, **Cold**, or **Moderate**.  

It mimics a simple real-world data analysis process:  
1. **Collect data** (temperatures).  
2. **Analyze data** (find max, min, average).  
3. **Classify data** (Hot / Cold / Moderate).  
4. **Interpret results** (summaries, reports).  

## Features

- Store Weekly Data – Record 7 days of temperature readings.  
- Basic Statistics – Quickly find maximum, minimum, and average temperature.  
- Day Categorization – Automatically label each day as **Hot**, **Cold**, or **Moderate**.  
- Database Integration (Optional) – Save results into a simple `WeatherData` table.  
- Summary Reports – Generate clear summaries of weather trends for the week.  
- Extensible Design– Can be extended to handle monthly/yearly data, or even live weather APIs.  
- Beginner-Friendly Analytics – Introduces the mindset of **data collection → analysis → categorization → interpretation**.

## Project Structure

WeatherDataAnalyzer/
│
|---src/            #core application logic
|    |---logic.py   #Business logic and task
operations
|    |___db.py      #Database operations
|
|----api/           # Backend API
|    |_main.py      # FastAPI endpoints
|
|----frontend/      # Frontend application
|     |__app.py     # Streamlit web interface
|
|____requirements.txt # Python Dependencies
|
|____README.md  # Project documentation
|
|____.env  # Python Variables

## Quick Start

### prerequisites

- Python 3.8 or higher
- A supabase account
- Git(Push,cloning)

### 1.clone or  Download the Project

# option 1: clone with Git
git clone <repository-url>

# option 2: Download and extract the ZIP file

### 2 . Install Dependencies

# Install all required Python packages
pip install -r requirements.txt

### 3 . set Up Supabase Database

1. Create a Supabase Project:

2. Create the Table Table:

- Go to the SQL Editor in your Supabase
dashboard
- Run this SQL command:
    '''sql
    CREATE TABLE WeatherData(
     id serial primary key,
     day varchar(10) not null,
     temperature float not null,
     category varchar(15)
);

'''
3. **Get Your Credentials:

### 4. Configure Environment Variables

1. Create a '.env' file in the project root

2. Add your Supabase creedentials to '.env':
SUPABASE_URL=your_project_url_here
SUPABASE_KEY=your_anon_key_here

### 5. Run the Application

## streamlit Frontend
streamlit run frontend/app.py

The app will open in your browser at 'http://localhost:8501'

## FastAPI Backend

cd api 
python main.py

THE API will be available at 'http://localhost:8000'

## How to Use 

## Technical Details 

### Technologies used 

- **Frontend** : Streamlit (Python web framework)
-**Backend** : FastAPI (Python REST API framework)
-**Database** : supabase (postgreSQL-based backend -as-a-service)
-**Language** : Python 3.8+

### Key Components

1. **'src/db.py'** : Database operations
-Handles all CRUD operations with supabase

2. **'src/logic.py'**: Business logic 
Task validation and processing

## Troubleshooting

## common Issues 

1. **'Module not found Errors**:

## Future Enhancements

Ideas for extending this project:

- **Live Weather Data** – Integrate with APIs (like OpenWeather) to fetch real-time weather.  
- **Data Visualization** – Add charts and graphs (using Matplotlib/Seaborn) to show temperature trends.  
- **Advanced Database** – Extend database design to handle multiple cities, sensors, or longer time periods.  
-  **Monthly & Yearly Analysis** – Analyze trends across weeks, months, or years instead of just 7 days.  
- **Machine Learning Predictions** – Predict future temperatures or classify weather using ML models.  
- **Web / Mobile App Interface** – Build a simple Flask/Django web app or mobile app to view reports.  
- **Alerts & Notifications** – Send alerts for extreme weather (too hot/too cold) via email or app notifications.  

## Support

If you encounter any issues or have questions: 
-mail id->abhinavvalaboju2005@gmail.com
-phone no: 



