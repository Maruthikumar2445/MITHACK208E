from typing import Dict, Any

class MockDataProvider:
    @staticmethod
    def get_mock_weather() -> Dict[str, Any]:
        return {
            "main": {
                "temp": 28.5,
                "humidity": 65,
                "pressure": 1012
            },
            "wind": {
                "speed": 3.6
            },
            "weather": [
                {
                    "description": "partly cloudy"
                }
            ],
            "dt": 1711766400  # March 30, 2025
        }

    @staticmethod
    def get_mock_soil_data() -> Dict[str, Any]:
        return {
            "properties": {
                "BLDFIE": {"values": [1.3, 1.4, 1.35]},
                "CLYPPT": {"values": [25, 27, 26]},
                "SNDPPT": {"values": [40, 38, 39]},
                "SLTPPT": {"values": [35, 35, 35]},
                "ORCDRC": {"values": [0.8, 0.75, 0.85]}
            }
        }