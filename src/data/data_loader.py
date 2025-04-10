"""
Data loading utilities for soil moisture data.
"""

import os
import logging
from typing import List, Dict, Optional, Tuple, Union, Any

import numpy as np
import pandas as pd
import geopandas as gpd
from pathlib import Path

import sys
sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))
import config


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("data_loader.log")
    ]
)
logger = logging.getLogger(__name__)


class SoilMoistureDataLoader:
    """
    A class to load soil moisture data from various sources.
    """

    def __init__(self, data_path: Optional[str] = None) -> None:
        """
        Initialize the data loader.

        Args:
            data_path: Path to the soil moisture data CSV file.
                      If None, the default path from config will be used.
        """
        self.data_path: str | Any = data_path or config.MOISTURE_DATA_PATH
        self.data = None
        self.geo_data = None

