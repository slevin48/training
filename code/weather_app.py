import streamlit as st
import datetime
from streamlit_folium import st_folium
import folium

def display_weather(data):
    st.title(f"Weather in {data['name']}, {data['sys']['country']}")

    # Map
    m = folium.Map(location=[data['coord']['lat'], data['coord']['lon']], zoom_start=10)
    folium.Marker([data['coord']['lat'], data['coord']['lon']], 
                  popup=f"{data['name']}").add_to(m)
    st_folium(m, width=700, height=500)

    # Sidebar
    with st.sidebar:
        st.subheader("Weather Details")

        # Main Weather Description
        weather = data['weather'][0]
        st.write(f"**Condition**: {weather['main']}")
        st.write(f"{weather['description'].capitalize()}")
        
        # Temperature in Celsius
        temp = data['main']
        temp_celsius = lambda k: k - 273.15
        st.metric("Temperature", f"{temp_celsius(temp['temp']):.2f} °C", delta=f"Min: {temp_celsius(temp['temp_min']):.2f} °C | Max: {temp_celsius(temp['temp_max']):.2f} °C")
        
        # Additional details
        st.write("**Details**:")
        st.write(f"- Pressure: {temp['pressure']} hPa")
        st.write(f"- Humidity: {temp['humidity']}%")

        # Visibility and Wind
        st.write(f"**Visibility**: {data['visibility']} meters")
        wind = data['wind']
        st.write(f"**Wind**: {wind['speed']} m/s at {wind['deg']}°")

        # Cloud Cover
        st.write(f"**Cloud Cover**: {data['clouds']['all']}%")

        # Sunrise and Sunset
        sunrise = datetime.datetime.fromtimestamp(data['sys']['sunrise'])
        sunset = datetime.datetime.fromtimestamp(data['sys']['sunset'])
        st.write(f"**Sunrise**: {sunrise.strftime('%H:%M:%S')} UTC")
        st.write(f"**Sunset**: {sunset.strftime('%H:%M:%S')} UTC")

# Sample data from OpenWeatherMap API
data = {
    "coord": {
        "lon": -0.13,
        "lat": 51.51
    },
    "weather": [
        {
            "id": 300,
            "main": "Drizzle",
            "description": "light intensity drizzle",
            "icon": "09d"
        }
    ],
    "base": "stations",
    "main": {
        "temp": 280.32,
        "pressure": 1012,
        "humidity": 81,
        "temp_min": 279.15,
        "temp_max": 281.15
    },
    "visibility": 10000,
    "wind": {
        "speed": 4.1,
        "deg": 80
    },
    "clouds": {
        "all": 90
    },
    "dt": 1485789600,
    "sys": {
        "type": 1,
        "id": 5091,
        "message": 0.0103,
        "country": "GB",
        "sunrise": 1485762037,
        "sunset": 1485794875
    },
    "id": 2643743,
    "name": "London",
    "cod": 200
}

# Display the weather data
display_weather(data)
