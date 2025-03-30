import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from typing import Dict, List, Any

class AgriculturalAnalyzer:
    def __init__(self):
        self.scaler = StandardScaler()
        
    def analyze_crop_conditions(self, 
                              weather_data: pd.DataFrame, 
                              soil_data: pd.DataFrame) -> Dict[str, Any]:
        """
        Analyze crop growing conditions based on weather and soil data
        """
        conditions = {
            'temperature_status': self._analyze_temperature(weather_data),
            'moisture_status': self._analyze_moisture(weather_data, soil_data),
            'soil_health': self._analyze_soil_health(soil_data),
            'recommendations': []
        }
        
        # Generate recommendations based on conditions
        conditions['recommendations'] = self._generate_recommendations(conditions)
        return conditions
    
    def _analyze_temperature(self, weather_data: pd.DataFrame) -> str:
        temp = weather_data['temperature'].iloc[-1]
        if temp < 10:
            return "Too Cold"
        elif temp > 35:
            return "Too Hot"
        return "Optimal"
    
    def _analyze_moisture(self, 
                         weather_data: pd.DataFrame, 
                         soil_data: pd.DataFrame) -> str:
        humidity = weather_data['humidity'].iloc[-1]
        soil_moisture = soil_data['bulk_density'].iloc[-1]
        
        # Combined moisture analysis
        if humidity < 30 and soil_moisture < 1.2:
            return "Dry"
        elif humidity > 80 and soil_moisture > 1.6:
            return "Waterlogged"
        return "Adequate"
    
    def _analyze_soil_health(self, soil_data: pd.DataFrame) -> str:
        organic_carbon = soil_data['organic_carbon'].iloc[-1]
        if organic_carbon < 0.5:
            return "Poor"
        elif organic_carbon < 0.75:
            return "Moderate"
        return "Good"
    
    def _generate_recommendations(self, conditions: Dict[str, str]) -> List[str]:
        recommendations = []
        
        if conditions['temperature_status'] == "Too Hot":
            recommendations.append("Consider shade cultivation or protective measures")
        elif conditions['temperature_status'] == "Too Cold":
            recommendations.append("Use greenhouse or cold protection techniques")
            
        if conditions['moisture_status'] == "Dry":
            recommendations.append("Increase irrigation frequency")
        elif conditions['moisture_status'] == "Waterlogged":
            recommendations.append("Improve drainage and reduce watering")
            
        if conditions['soil_health'] == "Poor":
            recommendations.append("Add organic matter and implement crop rotation")
            
        return recommendations