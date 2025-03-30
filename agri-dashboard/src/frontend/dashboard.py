import streamlit as st
import pandas as pd
from datetime import datetime
from PIL import Image
import sys
import os

# Add parent directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from api.weather import WeatherAPI 
from api.soil import SoilAPI
from api.mock_data import MockDataProvider

def main():
    st.set_page_config(page_title="Agri Dashboard", layout="wide")
    
    # Initialize APIs with mock data
    weather_api = WeatherAPI()
    soil_api = SoilAPI()
    mock_data = MockDataProvider()
    
    # Sidebar
    st.sidebar.title("Agriculture Dashboard")
    menu = st.sidebar.selectbox(
        "Select Module",
        ["Weather Info", "Soil Analysis", "Crop Health", "Pest Detection"]
    )
    
    # Default location
    lat = st.sidebar.number_input("Latitude", value=20.5937)
    lon = st.sidebar.number_input("Longitude", value=78.9629)
    
    if menu == "Weather Info":
        st.title("Weather Information")
        if st.button("Get Weather Data"):
            weather_data = weather_api.get_current_weather(lat, lon)
            
            col1, col2 = st.columns(2)
            with col1:
                st.metric("Temperature", f"{weather_data['main']['temp']}°C")
                st.metric("Humidity", f"{weather_data['main']['humidity']}%")
            
            with col2:
                st.metric("Wind Speed", f"{weather_data['wind']['speed']} m/s")
                st.metric("Weather", weather_data['weather'][0]['description'].title())
    
    elif menu == "Soil Analysis":
        st.title("Soil Analysis")
        if st.button("Analyze Soil"):
            soil_data = soil_api.get_soil_data(lat, lon)
            
            col1, col2 = st.columns(2)
            with col1:
                st.metric("Bulk Density", f"{soil_data['properties']['BLDFIE']['values'][0]:.2f} g/cm³")
                st.metric("Clay Content", f"{soil_data['properties']['CLYPPT']['values'][0]}%")
            
            with col2:
                st.metric("Sand Content", f"{soil_data['properties']['SNDPPT']['values'][0]}%")
                st.metric("Organic Carbon", f"{soil_data['properties']['ORCDRC']['values'][0]}%")
    
    elif menu == "Crop Health":
        st.title("Crop Health Analysis")
        uploaded_file = st.file_uploader("Upload crop image", type=['jpg', 'png'])
        
        if uploaded_file:
            image = Image.open(uploaded_file)
            st.image(image, caption="Uploaded Image")
            
            if st.button("Analyze Crop Health"):
                st.info("Using mock data for crop health analysis")
                st.success("Crop appears healthy with good growth patterns")
                st.write("Recommendations:")
                st.write("- Maintain current irrigation schedule")
                st.write("- Monitor for early signs of nutrient deficiency")
    
    elif menu == "Pest Detection":
        st.title("Pest Detection")
        uploaded_file = st.file_uploader("Upload image for pest detection", type=['jpg', 'png'])
        
        if uploaded_file:
            image = Image.open(uploaded_file)
            st.image(image, caption="Uploaded Image")
            
            if st.button("Detect Pests"):
                st.info("Using mock data for pest detection")
                st.write("No significant pest infestations detected")
                st.write("Preventive Measures:")
                st.write("- Regular monitoring")
                st.write("- Maintain field hygiene")

if __name__ == "__main__":
    main()