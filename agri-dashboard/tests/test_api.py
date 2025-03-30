import pytest
from src.api.weather import WeatherAPI
import os

def test_weather_api_initialization():
    api_key = "test_key"
    weather_api = WeatherAPI(api_key)
    assert weather_api.api_key == api_key
    assert weather_api.base_url == "http://api.openweathermap.org/data/2.5"

@pytest.mark.integration
def test_get_current_weather():
    api_key = os.getenv("OPENWEATHER_API_KEY")
    weather_api = WeatherAPI(api_key)
    
    # Test with Delhi coordinates
    lat, lon = 28.6139, 77.2090
    response = weather_api.get_current_weather(lat, lon)
    
    assert isinstance(response, dict)
    assert "main" in response
    assert "temp" in response["main"]
    assert "humidity" in response["main"]

@pytest.mark.integration
def test_get_forecast():
    api_key = os.getenv("OPENWEATHER_API_KEY")
    weather_api = WeatherAPI(api_key)
    
    lat, lon = 28.6139, 77.2090
    days = 5
    response = weather_api.get_forecast(lat, lon, days)
    
    assert isinstance(response, dict)
    assert "list" in response
    assert len(response["list"]) == days * 8