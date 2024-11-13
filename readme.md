# Car Price Prediction App

This application provides an interactive tool for predicting car prices based on user inputs. It is built using Streamlit and connects to a machine learning model API hosted on Render.

## Features

- **User Inputs**: Users can enter details such as the car's year, engine size, mileage, type, make, and options to get an estimated price range.
- **Real-Time Prediction**: Upon clicking "Predict Price," the app sends data to an API endpoint, which returns a price category prediction (Cheap, Good, or High).
- **Error Handling**: Displays an error message if the API request fails.

## How It Works

1. **User Inputs**: Collects essential car information:
   - **Year** (1980-2024)
   - **Engine Size** in Liters
   - **Mileage** in kilometers
   - **Car Type** (e.g., Accent, Land Cruiser)
   - **Make** (e.g., Hyundai, Mercedes)
   - **Options** (e.g., Full, Standard)

2. **API Prediction Request**: Once the "Predict Price" button is clicked:
   - The app sends a POST request to `https://the-penguin.onrender.com/predict`, providing the car details in JSON format.
   - The API returns a prediction:
     - `0` for **Cheap Price**
     - `1` for **Good Price**
     - `2` for **High Price**

3. **Display Result**: The prediction is displayed as an estimated price category on the app.

## Installation and Setup

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-name>

2. Install required packages:
   ```bash
   pip install streamlit requests
   ```
3. Run the app
  ```bash
  streamlit run app.py
   ```

Just copy and paste this into your README file, and it will display similarly. Let me know if you need further help!

## Requirements

- **Streamlit**: For the front-end interface.
- **Requests**: To handle API requests.

## Example

1. Start the Streamlit app.
2. Enter the required car details.
3. Click "Predict Price" to receive the price category prediction.

## Notes

- Ensure the API endpoint `https://the-penguin.onrender.com/predict` is active for the app to work correctly.
- This app uses a mock API for educational purposes; adapt the endpoint and data as needed for other predictive models.

## Future Improvements

- **Expand Car Types and Makes**: Add more car models and makes to cover a broader range.
- **Include Additional Features**: Add inputs such as color, condition, or location for a more accurate prediction.
- **Enhance Model Integration**: Update the API endpoint to a more robust model as necessary.
