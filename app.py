import streamlit as st
import pandas as pd
import joblib as j

# Load the pre-trained Linear Regression model
model = j.load('LinearRegressionModel.h5')

def predict_price(inputs):
    """
    This function takes a DataFrame of input features and returns the predicted house price.
    :param inputs: DataFrame of input features
    :return: Predicted house price
    """
    prediction = model.predict(inputs)
    return prediction

def main():
    """
    This is the main function that runs the Streamlit app.
    """
    # Set the title of the app
    st.title('California House Price Prediction App 🚀')
    
    # Set the header for the sidebar
    st.sidebar.header('Input Data for House Price Prediction')
    
    # Create a dictionary to store the input features
    input_features = {}
    
    # Add input widgets to the sidebar to collect user inputs
    input_features['longitude'] = st.sidebar.number_input('Longitude', -180.0, 180.0, 0.0)
    input_features['latitude'] = st.sidebar.number_input('Latitude', -90.0, 90.0, 0.0)
    input_features['housing_median_age'] = st.sidebar.slider('Housing Median Age', 0, 100, 30)
    input_features['total_rooms'] = st.sidebar.number_input('Total Rooms', min_value=1)
    input_features['total_bedrooms'] = st.sidebar.number_input('Total Bedrooms', min_value=1)
    input_features['population'] = st.sidebar.number_input('Population', min_value=1)
    input_features['households'] = st.sidebar.number_input('Households', min_value=1)
    input_features['median_income'] = st.sidebar.number_input('Median Income', min_value=0.0)
    
    # Add checkboxes for categorical features
    input_features['<1H OCEAN'] = st.sidebar.checkbox('<1H OCEAN')
    input_features['INLAND'] = st.sidebar.checkbox('INLAND')
    input_features['NEAR BAY'] = st.sidebar.checkbox('NEAR BAY')
    input_features['NEAR OCEAN'] = st.sidebar.checkbox('NEAR OCEAN')
    
    # Create a DataFrame from the dictionary of input features
    input_df = pd.DataFrame([input_features])
    
    # Display the input data on the app
    st.write('### Input Data for House Price Prediction:')
    st.write(input_df)
    
    # Make a prediction using the pre-trained model and display the result
    prediction = predict_price(input_df)
    st.write(f'## Estimated House Price: {prediction}')

if __name__ == '__main__':
    main()
