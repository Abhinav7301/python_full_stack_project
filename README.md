# Weather Data Analysis

## Overview

This project focuses on **analyzing a week's temperature data**. It stores daily temperature readings, calculates basic statistics, and classifies days as **Hot**, **Cold**, or **Moderate**. The project mimics a real-world data analysis workflow: collecting data, analyzing it, categorizing days, and interpreting results.

## Features

- **Store Weekly Data**: Record temperature readings for 7 days.
- **Basic Statistics**: Calculate maximum, minimum, and average temperatures.
- **Day Categorization**: Label each day as **Hot**, **Cold**, or **Moderate**.
- **Database Integration (Optional)**: Store results in a `WeatherData` table using Supabase.
- **Summary Reports**: Generate clear summaries of weekly weather trends.
- **Extensible Design**: Easily extendable for monthly/yearly data or live weather APIs.
- **Beginner-Friendly Analytics**: Introduces data collection, analysis, categorization, and interpretation.

## Project Structure

```
WeatherDataAnalyzer/
│
├── src/                    # Core application logic
│   ├── logic.py            # Business logic and task operations
│   └── db.py               # Database operations
│
├── api/                    # Backend API
│   └── main.py             # FastAPI endpoints
│
├── frontend/               # Frontend application
│   └── app.py              # Streamlit web interface
│
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
└── .env                    # Environment variables
```

## Quick Start

### Prerequisites

- **Python**: Version 3.8 or higher
- **Supabase Account**: For database integration
- **Git**: For cloning and pushing to the repository

### 1. Clone or Download the Project

```bash
# Option 1: Clone with Git
git clone <repository-url>

# Option 2: Download and extract the ZIP file
```

### 2. Install Dependencies

```bash
# Install all required Python packages
pip install -r requirements.txt
```

### 3. Set Up Supabase Database

1. **Create a Supabase Project**:
   - Sign up at [Supabase](https://supabase.com/) and create a new project.

2. **Create the `WeatherData` Table**:
   - Navigate to the SQL Editor in your Supabase dashboard.
   - Run the following SQL command:

```sql
CREATE TABLE WeatherData (
    id SERIAL PRIMARY KEY,
    day VARCHAR(10) NOT NULL,
    temperature FLOAT NOT NULL,
    category VARCHAR(15)
);
```

3. **Get Your Credentials**:
   - Copy your Supabase project URL and anon key from the Supabase dashboard.

### 4. Configure Environment Variables

1. Create a `.env` file in the project root.
2. Add your Supabase credentials to the `.env` file:

```
SUPABASE_URL=your_project_url_here
SUPABASE_KEY=your_anon_key_here
```

### 5. Run the Application

#### Streamlit Frontend
```bash
streamlit run frontend/app.py
```
The app will open in your browser at `http://localhost:8501`.

#### FastAPI Backend
```bash
cd api
python main.py
```
The API will be available at `http://localhost:8000`.

## How to Use

1. **Frontend**: Use the Streamlit interface to input temperature data, view statistics, and generate reports.
2. **Backend**: Interact with the FastAPI endpoints to perform CRUD operations on the `WeatherData` table.
3. **Database**: Store and retrieve temperature data using Supabase.

## Technical Details

### Technologies Used

- **Frontend**: Streamlit (Python web framework)
- **Backend**: FastAPI (Python REST API framework)
- **Database**: Supabase (PostgreSQL-based backend-as-a-service)
- **Language**: Python 3.8+

### Key Components

1. **`src/db.py`**:
   - Handles all CRUD operations with Supabase.
2. **`src/logic.py`**:
   - Contains business logic for data validation, statistics calculation, and day categorization.

## Troubleshooting

### Common Issues

1. **Module Not Found Errors**:
   - Ensure all dependencies are installed using `pip install -r requirements.txt`.
   - Verify that Python 3.8+ is installed and active.

2. **Supabase Connection Issues**:
   - Double-check your `.env` file for correct `SUPABASE_URL` and `SUPABASE_KEY`.
   - Ensure your Supabase project is active and the `WeatherData` table exists.

3. **Streamlit or FastAPI Not Running**:
   - Confirm the correct ports (`8501` for Streamlit, `8000` for FastAPI) are not in use.
   - Check for errors in the terminal and resolve missing dependencies.

## Future Enhancements

- **Live Weather Data**: Integrate APIs like OpenWeather to fetch real-time weather data.
- **Data Visualization**: Add charts and graphs using Matplotlib or Seaborn for temperature trends.
- **Advanced Database**: Support multiple cities, sensors, or extended time periods.
- **Monthly & Yearly Analysis**: Analyze trends over weeks, months, or years.
- **Machine Learning Predictions**: Predict future temperatures or classify weather using ML models.
- **Web/Mobile App Interface**: Build a Flask/Django web app or mobile app for reports.
- **Alerts & Notifications**: Send alerts for extreme weather via email or app notifications.

## Support

For issues or questions, contact:
- **Email**: abhinavvalaboju2005@gmail.com
- **Phone**: +91 8555828332




