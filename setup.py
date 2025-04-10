from setuptools import find_packages, setup

setup(
    name="soil_health_monitoring",
    version="0.1.0",
    description="A tool for monitoring soil health and sustainability using volumetric soil moisture data",
    author="Nishant Gupta",
    author_email="shub002gupta@gmail.com",
    packages=find_packages(),
    python_requires=">=3.9",
    include_package_data=True,
    install_requires=[
        "numpy>=1.24.0",
        "pandas>=2.0.0",
        "scikit-learn>=1.3.0",
        "scipy>=1.11.0",
        "xgboost>=1.7.0",
        "statsmodels>=0.14.0",
        "geopandas>=0.13.0",
        "folium>=0.14.0",
        "matplotlib>=3.7.0",
        "seaborn>=0.12.0",
        "plotly>=5.16.0",
        "flask>=2.3.0",
        "flask-restful>=0.3.10",
        "flask-sqlalchemy>=3.0.0",
        "sqlalchemy>=2.0.0",
        "python-dotenv>=1.0.0",
        "pyyaml>=6.0.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.4.0",
            "pytest-cov>=4.1.0",
            "black>=23.7.0",
            "flake8>=6.1.0",
            "mypy>=1.5.0",
            "isort>=5.12.0",
            "pre-commit>=3.3.3",
        ],
    },
    entry_points={
        "console_scripts": [
            "soil-health-app=app.main:main",
        ],
    },
)
