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

# src/frontend/components/maps.py

import streamlit as st
import folium
from streamlit_folium import folium_static
from typing import Tuple

class MapComponent:
    def __init__(self):
        self.default_location = (20.5937, 78.9629)  # India's center
        self.default_zoom = 5

    def display_map(self, center: Tuple[float, float] = None, zoom: int = None) -> None:
        """Display an interactive map with weather and soil data overlay"""
        center = center or self.default_location
        zoom = zoom or self.default_zoom

        m = folium.Map(location=center, zoom_start=zoom)
        
        # Add tile layer
        folium.TileLayer(
            'OpenStreetMap',
            name='OpenStreetMap'
        ).add_to(m)

        # Add marker for selected location
        folium.Marker(
            center,
            popup='Selected Location',
            icon=folium.Icon(color='red', icon='info-sign')
        ).add_to(m)

        # Display the map in Streamlit
        folium_static(m)

    def add_weather_overlay(self, m: folium.Map, weather_data: dict) -> None:
        """Add weather data overlay to the map"""
        temp = weather_data['main']['temp']
        humidity = weather_data['main']['humidity']
        
        popup_html = f"""
        <div style='font-family: Arial'>
            <h4>Weather Information</h4>
            <p>Temperature: {temp}°C</p>
            <p>Humidity: {humidity}%</p>
        </div>
        """
        
        folium.CircleMarker(
            location=(weather_data['coord']['lat'], weather_data['coord']['lon']),
            radius=30,
            popup=folium.Popup(popup_html, max_width=300),
            color='#3186cc',
            fill=True,
            fill_color='#3186cc'
        ).add_to(m)