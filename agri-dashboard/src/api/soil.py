import requests
from typing import Dict, Any
from .mock_data import MockDataProvider

class SoilAPI:
    def __init__(self):
        self.base_url = "https://rest.soilgrids.org/query"
        self.mock_data = MockDataProvider()
        self.use_mock = True

    def get_soil_data(self, lat: float, lon: float) -> Dict[str, Any]:
        if self.use_mock:
            return self.mock_data.get_mock_soil_data()
        
        params = {
            "lat": lat,
            "lon": lon,
            "attributes": ["BLDFIE", "CLYPPT", "SNDPPT", "SLTPPT", "ORCDRC"],
            "depths": [0, 30, 60]
        }
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json"
        }
        response = requests.get(self.base_url, params=params, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Soil API Error: {response.status_code}")