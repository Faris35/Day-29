# Import required libraries
import streamlit as st
import requests

# Define the URL of your API
url = "https://the-penguin.onrender.com/predict"

# Title of the app
st.title("Car Price Prediction")

# Create input fields for each parameter
year = st.number_input("Year", min_value=1900, max_value=2025, value=2020, step=1)
engine_size = st.number_input("Engine Size (in Liters)", min_value=0.5, max_value=10.0, value=2.5, step=0.1)
mileage = st.number_input("Mileage", min_value=0, max_value=300000, value=15000, step=1000)
car_type = st.text_input("Type", value="Accent")
make = st.text_input("Make", value="Hyundai")
options = st.text_input("Options", value="Full")

# Button to trigger the API call
if st.button("Predict Price"):
    # Define the parameters
    params = {
        "Year": year,
        "Engine_Size": engine_size,
        "Mileage": mileage,
        "Type": car_type,
        "Make": make,
        "Options": options
    }

    # Call the API
    response = requests.get(url, params=params)
    
    # Check if the response is successful
    if response.status_code == 200:
        prediction = response.json()  # Assuming the response returns a JSON
        st.success(f"Predicted Price: ${prediction.get('price', 'N/A')}")
    else:
        st.error("Failed to fetch prediction. Please try again later.")
