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
│   │   └── analysis.py
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

src/models/crop_health.py
```python
import requests
import base64
from typing import Dict, Any
from PIL import Image
import io

class CropHealthAnalyzer:
    def __init__(self, api_key: str, endpoint: str):
        self.api_key = api_key
        self.endpoint = endpoint
        self.headers = {
            "api-key": self.api_key,
            "Content-Type": "application/json"
        }

    def _encode_image(self, image_path: str) -> str:
        """Convert image to base64 string"""
        with Image.open(image_path) as img:
            buffered = io.BytesIO()
            img.save(buffered, format="JPEG")
            return base64.b64encode(buffered.getvalue()).decode()

    def analyze_crop(self, image_path: str) -> Dict[str, Any]:
        """Analyze crop health using Llama Vision model"""
        base64_image = self._encode_image(image_path)
        
        payload = {
            "messages": [
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": "Analyze this crop image for health issues, diseases, and provide recommendations"
                        },
                        {
                            "type": "image_url",
                            "image_url": f"data:image/jpeg;base64,{base64_image}"
                        }
                    ]
                }
            ]
        }

        response = requests.post(self.endpoint, headers=self.headers, json=payload)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Vision API Error: {response.status_code}")