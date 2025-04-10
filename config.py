import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Base directory of the project
BASE_DIR = Path(__file__).resolve().parent

# Data directories
DATA_DIR = os.path.join(BASE_DIR, "data")
RAW_DATA_DIR = os.path.join(DATA_DIR, "raw")
PROCESSED_DATA_DIR = os.path.join(DATA_DIR, "processed")

# Ensure directories exist
os.makedirs(RAW_DATA_DIR, exist_ok=True)
os.makedirs(PROCESSED_DATA_DIR, exist_ok=True)

# Input data files
MOISTURE_DATA_PATH = os.path.join(RAW_DATA_DIR, "soil_moisture_data.csv")

# Model directories
MODEL_DIR = os.path.join(BASE_DIR, "models")
os.makedirs(MODEL_DIR, exist_ok=True)

# Application settings
DEBUG = os.getenv("DEBUG", "False").lower() in ("true", "1", "t")
FLASK_ENV = os.getenv("FLASK_ENV", "production")
SECRET_KEY = os.getenv("SECRET_KEY", "default-secret-key-for-development")
DATABASE_URI = os.getenv(
    "DATABASE_URI", f"sqlite:///{os.path.join(BASE_DIR, 'soil_health.db')}"
)

# Soil health thresholds
# These thresholds are based on common agricultural standards and can be adjusted
SOIL_MOISTURE_THRESHOLDS = {
    "critical_low": 0.15,  # Critical low soil moisture (m³/m³)
    "low": 0.25,  # Low soil moisture (m³/m³)
    "optimal_min": 0.30,  # Minimum optimal soil moisture (m³/m³)
    "optimal_max": 0.45,  # Maximum optimal soil moisture (m³/m³)
    "high": 0.50,  # High soil moisture (m³/m³)
    "critical_high": 0.60,  # Critical high soil moisture (m³/m³)
}

# Time periods for trend analysis
TREND_PERIODS = {
    "short_term": 30,  # 30 days
    "medium_term": 90,  # 90 days
    "long_term": 365,  # 1 year
    "historical": 1095,  # 3 years
}

# Model parameters
MODEL_PARAMS = {
    "xgboost": {
        "n_estimators": 100,
        "learning_rate": 0.1,
        "max_depth": 5,
        "subsample": 0.8,
        "colsample_bytree": 0.8,
        "objective": "reg:squarederror",
        "seed": 42,
    },
    "lstm": {
        "units": 50,
        "dropout": 0.2,
        "recurrent_dropout": 0.2,
        "epochs": 100,
        "batch_size": 32,
        "patience": 10,
    },
    "prophet": {
        "changepoint_prior_scale": 0.05,
        "seasonality_prior_scale": 10.0,
        "seasonality_mode": "multiplicative",
        "daily_seasonality": False,
        "weekly_seasonality": True,
        "yearly_seasonality": True,
    },
}
