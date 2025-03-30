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
│   │       ├── charts.py
│   │       └── chart_component.py
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
```

Content of `chart_component.py`:
```python
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from typing import List, Dict, Any
import pandas as pd

class ChartComponent:
    def plot_weather_trends(self, weather_data: pd.DataFrame) -> None:
        """Plot weather trends using Plotly"""
        fig = go.Figure()
        
        # Temperature line
        fig.add_trace(go.Scatter(
            x=weather_data['timestamp'],
            y=weather_data['temperature'],
            name='Temperature (°C)',
            line=dict(color='red')
        ))
        
        # Humidity line
        fig.add_trace(go.Scatter(
            x=weather_data['timestamp'],
            y=weather_data['humidity'],
            name='Humidity (%)',
            line=dict(color='blue')
        ))
        
        fig.update_layout(
            title='Weather Trends',
            xaxis_title='Time',
            yaxis_title='Value',
            hovermode='x unified'
        )
        
        st.plotly_chart(fig)
    
    def plot_soil_composition(self, soil_data: pd.DataFrame) -> None:
        """Create a pie chart for soil composition"""
        labels = ['Sand', 'Silt', 'Clay']
        values = [
            soil_data['sand_content'].iloc[-1],
            soil_data['silt_content'].iloc[-1],
            soil_data['clay_content'].iloc[-1]
        ]
        
        fig = px.pie(
            values=values,
            names=labels,
            title='Soil Composition'
        )
        
        st.plotly_chart(fig)
    
    def plot_crop_health_metrics(self, analysis_results: Dict[str, Any]) -> None:
        """Create a radar chart for crop health metrics"""
        categories = ['Temperature', 'Moisture', 'Soil Health', 'Pest Risk', 'Disease Risk']
        
        fig = go.Figure()
        
        fig.add_trace(go.Scatterpolar(
            r=[
                analysis_results['temperature_score'],
                analysis_results['moisture_score'],
                analysis_results['soil_health_score'],
                analysis_results['pest_risk_score'],
                analysis_results['disease_risk_score']
            ],
            theta=categories,
            fill='toself',
            name='Current Status'
        ))
        
        fig.update_layout(
            polar=dict(
                radialaxis=dict(
                    visible=True,
                    range=[0, 10]
                )
            ),
            showlegend=False,
            title='Crop Health Analysis'
        )
        
        st.plotly_chart(fig)