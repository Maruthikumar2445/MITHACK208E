agri-dashboard
├── src
│   ├── api
│   │   ├── weather.py
│   │   ├── soil.py
│   │   └── nasa.py
│   ├── models
│   │   ├── crop_health.py
│   │   ├── irrigation.py
│   │   └── pest_detection.py
│   ├── data_processing
│   │   ├── preprocessing.py
│   │   ├── analysis.py
│   │   └── data_processor.py
│   ├── frontend
│   │   ├── dashboard.py
│   │   └── components
│   │       ├── maps.py
│   │       └── charts.py
│   ├── utils
│   │   ├── geospatial.py
│   │   └── helpers.py
│   └── main.py
├── tests
│   ├── test_api.py
│   ├── test_models.py
│   └── test_processing.py
├── requirements.txt
├── config.yaml
└── README.md

# src/data_processing/data_processor.py
import pandas as pd
import numpy as np
from typing import Dict, Any

class DataProcessor:
    @staticmethod
    def process_weather_data(weather_data: Dict[str, Any]) -> pd.DataFrame:
        """Process raw weather data into structured format"""
        data = {
            'temperature': weather_data['main']['temp'],
            'humidity': weather_data['main']['humidity'],
            'pressure': weather_data['main']['pressure'],
            'wind_speed': weather_data['wind']['speed'],
            'description': weather_data['weather'][0]['description'],
            'timestamp': pd.to_datetime(weather_data['dt'], unit='s')
        }
        return pd.DataFrame([data])

    @staticmethod
    def process_soil_data(soil_data: Dict[str, Any]) -> pd.DataFrame:
        """Process raw soil data into structured format"""
        properties = soil_data['properties']
        data = {
            'bulk_density': np.mean(properties['BLDFIE']['values']),
            'clay_content': np.mean(properties['CLYPPT']['values']),
            'sand_content': np.mean(properties['SNDPPT']['values']),
            'silt_content': np.mean(properties['SLTPPT']['values']),
            'organic_carbon': np.mean(properties['ORCDRC']['values'])
        }
        return pd.DataFrame([data])