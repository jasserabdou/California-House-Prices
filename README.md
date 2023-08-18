# California House Price Prediction App

This Streamlit app predicts house prices in California based on user input features. The app utilizes a pre-trained Linear Regression model to make predictions.

## Deployed on Streamlit Community Cloud

This app has been deployed on the Streamlit Community Cloud and can be accessed using the following link: [California House Price Prediction App](https://share.streamlit.io/your-username/your-repo-name/main/app.py)

## Requirements

To run the app locally, you'll need to install the required dependencies specified in the `requirements.txt` file. You can install them using the following command:

```
pip install -r requirements.txt
```

## Usage

1. Clone this repository to your local machine.

2. Install the required dependencies as mentioned in the `requirements.txt` file.

3. Obtain the pre-trained Linear Regression model file (e.g., `LinearRegressionModel.h5`) and place it in the same directory as the `app.py` file.

4. Run the Streamlit app by executing the following command:

```
streamlit run app.py
```

5. The app will open in your web browser. You can input the desired features in the sidebar and see the estimated house price prediction.

## Features and Input

The app provides input fields for the following features:

- Longitude
- Latitude
- Housing Median Age
- Total Rooms
- Total Bedrooms
- Population
- Households
- Median Income

Additionally, you can select categorical features using checkboxes for the following ocean proximity options:

- <1H OCEAN
- INLAND
- NEAR BAY
- NEAR OCEAN


