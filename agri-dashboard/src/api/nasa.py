import requests

def get_historical_weather_data(latitude, longitude, start_date, end_date, api_key):
    url = f"https://power.larc.nasa.gov/api/temporal/daily/point?start={start_date}&end={end_date}&latitude={latitude}&longitude={longitude}&community=RE&format=JSON&parameters=TEMP,PRECIP"
    headers = {
        'Accept': 'application/json',
    }
    response = requests.get(url, headers=headers, params={'api_key': api_key})
    
    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()