import pytest
import pandas as pd
import numpy as np
from src.data_processing.analysis import AgriculturalAnalyzer

@pytest.fixture
def analyzer():
    return AgriculturalAnalyzer()

@pytest.fixture
def sample_weather_data():
    return pd.DataFrame({
        'temperature': [25.5, 26.0, 27.5],
        'humidity': [65, 70, 75],
        'timestamp': pd.date_range(start='2025-03-30', periods=3)
    })

@pytest.fixture
def sample_soil_data():
    return pd.DataFrame({
        'bulk_density': [1.3],
        'organic_carbon': [0.8],
        'sand_content': [40],
        'silt_content': [40],
        'clay_content': [20]
    })

def test_analyze_crop_conditions(analyzer, sample_weather_data, sample_soil_data):
    conditions = analyzer.analyze_crop_conditions(sample_weather_data, sample_soil_data)
    
    assert isinstance(conditions, dict)
    assert 'temperature_status' in conditions
    assert 'moisture_status' in conditions
    assert 'soil_health' in conditions
    assert 'recommendations' in conditions
    assert isinstance(conditions['recommendations'], list)