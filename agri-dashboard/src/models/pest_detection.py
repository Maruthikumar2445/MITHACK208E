import requests
import base64
from typing import Dict, Any
from PIL import Image
import io

class PestDetector:
    def __init__(self, api_key: str, endpoint: str):
        self.api_key = api_key
        self.endpoint = endpoint
        self.headers = {
            "api-key": self.api_key,
            "Content-Type": "application/json"
        }

    def _encode_image(self, image: Image.Image) -> str:
        buffered = io.BytesIO()
        image.save(buffered, format="JPEG")
        return base64.b64encode(buffered.getvalue()).decode()

    def detect_pests(self, image: Image.Image) -> Dict[str, Any]:
        base64_image = self._encode_image(image)
        
        payload = {
            "messages": [
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": "Analyze this image for pest infestations, identify the pests, and suggest treatment options"
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