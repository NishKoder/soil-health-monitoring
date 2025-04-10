# Soil Health Monitoring and Sustainability Tool

## Overview

This project provides a comprehensive solution for monitoring soil health and sustainability using volumetric soil moisture data. The tool is designed for environmental researchers, agronomists, and agricultural planners to study the impacts of agricultural practices and climate variability on soil quality.

The application leverages soil moisture data from the VIC model run by NRSC (National Remote Sensing Centre) for states/UTs and districts in India, available from 2018 onwards.

## Key Features

- **Data Processing**: Advanced algorithms for cleaning, normalizing, and transforming soil moisture data
- **Trend Analysis**: Track soil moisture changes to assess soil degradation or improvement over time
- **Sustainability Indicators**: Combine moisture data with other soil health metrics to produce sustainability scores
- **Visualization**: Interactive dashboards for visualizing soil health metrics across regions and time periods
- **Decision Support**: AI-driven recommendations for soil management practices that improve water retention
- **Real-time Monitoring**: Continuous tracking of soil moisture conditions with alerts for critical changes

## Installation

```bash
# Clone the repository
git clone https://github.com/username/soil-health-monitoring.git
cd soil-health-monitoring

# Create and activate virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install the package in development mode
pip install -e .
```

## Data

The dataset contains Volumetric Soil Moisture data for states/UTs and districts in India. The data is calculated based on the output of the VIC (Variable Infiltration Capacity) model run by NRSC and is available from 2018 onwards.

### Data Source
- Original data available at: [Kaggle - Daily Data of Soil Moisture](https://www.kaggle.com/datasets/vaibhavbajpai458/daily-data-of-soil-moisture)
- Download the dataset and place it in the `data/raw/` directory

## Usage

### Running the Analysis Notebooks

```bash
jupyter notebook notebooks/
```

### Starting the Web Application

```bash
cd app
python main.py
```

The application will be available at `http://localhost:5000/`

## Project Structure

- `data/`: Raw and processed data storage
- `notebooks/`: Jupyter notebooks for data exploration, preprocessing, and model development
- `src/`: Source code for data processing, feature engineering, modeling, and visualization
- `app/`: Web application for soil health monitoring and recommendations
- `tests/`: Unit tests for key components

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contributors

- [Your Name](https://github.com/yourusername)

## Acknowledgments

- National Remote Sensing Centre (NRSC) for providing the VIC model output data




soil_health_monitoring/
│
├── data/                              # Data storage
│   ├── raw/                           # Raw dataset files
│   └── processed/                     # Processed dataset files
│
├── notebooks/                         # Jupyter notebooks for analysis
│   ├── data_exploration.ipynb         # Initial data exploration
│   ├── data_preprocessing.ipynb       # Data cleaning and preparation
│   └── model_development.ipynb        # Model training and evaluation
│
├── src/                               # Source code
│   ├── __init__.py
│   ├── data/                          # Data processing modules
│   │   ├── __init__.py
│   │   ├── data_loader.py             # Data loading utilities
│   │   └── data_processor.py          # Data processing utilities
│   │
│   ├── features/                      # Feature engineering
│   │   ├── __init__.py
│   │   └── feature_engineering.py     # Feature creation and transformation
│   │
│   ├── models/                        # Model-related code
│   │   ├── __init__.py
│   │   ├── soil_health_model.py       # Soil health assessment model
│   │   └── trend_analysis.py          # Time series analysis for trends
│   │
│   ├── visualization/                 # Visualization utilities
│   │   ├── __init__.py
│   │   └── visualize.py               # Plotting functions
│   │
│   └── utils/                         # Utility functions
│       ├── __init__.py
│       └── helpers.py                 # Helper functions
│
├── app/                               # Web application
│   ├── __init__.py
│   ├── main.py                        # Main application entry point
│   ├── routes.py                      # Application routes
│   ├── static/                        # Static files (CSS, JS)
│   │   ├── css/
│   │   └── js/
│   └── templates/                     # HTML templates
│       ├── index.html
│       ├── analysis.html
│       └── recommendations.html
│
├── tests/                             # Unit tests
│   ├── __init__.py
│   ├── test_data_loader.py
│   └── test_soil_health_model.py
│
├── config.py                          # Configuration settings
├── requirements.txt                   # Project dependencies
├── setup.py                           # Package installation
└── README.md                          # Project documentation