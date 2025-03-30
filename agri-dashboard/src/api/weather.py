import requests
import json
from typing import Dict, Any
from .mock_data import MockDataProvider

class WeatherAPI:
    def __init__(self, api_key: str = None):
        self.mock_data = MockDataProvider()
        self.use_mock = api_key is None or api_key.startswith("YOUR_")
        self.api_key = api_key
        self.base_url = "http://api.openweathermap.org/data/2.5"

    def get_current_weather(self, lat: float, lon: float) -> Dict[str, Any]:
        """Get current weather data for given coordinates"""
        if self.use_mock:
            return self.mock_data.get_mock_weather()
        
        endpoint = f"{self.base_url}/weather"
        params = {
            "lat": lat,
            "lon": lon,
            "appid": self.api_key,
            "units": "metric"
        }
        
        response = requests.get(endpoint, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Weather API Error: {response.status_code}")

    def get_forecast(self, lat: float, lon: float, days: int = 5) -> Dict[str, Any]:
        """Get weather forecast for given coordinates"""
        endpoint = f"{self.base_url}/forecast"
        params = {
            "lat": lat,
            "lon": lon,
            "appid": self.api_key,
            "units": "metric",
            "cnt": days * 8  # 8 readings per day
        }
        
        response = requests.get(endpoint, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Forecast API Error: {response.status_code}")