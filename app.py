import streamlit as st
import pandas as pd
import joblib
from datetime import datetime

# Load the trained model
model = joblib.load('price_prediction_model.pkl')

# Function to preprocess input data
def preprocess_input(data):
    # Convert the input data to a DataFrame
    df = pd.DataFrame([data])
    
    # Add datetime features
    df['saleYear'] = pd.to_datetime(df['saledate']).dt.year
    df['saleMonth'] = pd.to_datetime(df['saledate']).dt.month
    df['saleDay'] = pd.to_datetime(df['saledate']).dt.day
    df['saleDayOfWeek'] = pd.to_datetime(df['saledate']).dt.dayofweek
    df['saleDayOfYear'] = pd.to_datetime(df['saledate']).dt.dayofyear
    
    # Drop the original saledate column
    df.drop('saledate', axis=1, inplace=True)
    
    # Fill missing numeric values with median
    for label, content in df.items():
        if pd.api.types.is_numeric_dtype(content):
            if pd.isnull(content).sum():
                df[label+'_is_missing'] = pd.isnull(content)
                df[label] = content.fillna(content.median())
    
    # Convert categorical variables to numbers
    for label, content in df.items():
        if not pd.api.types.is_numeric_dtype(content):
            df[label+'_is_missing'] = pd.isnull(content)
            df[label] = pd.Categorical(content).codes + 1
    
    return df

# Streamlit app
st.title('Bulldozer Price Prediction')

# Input fields
st.sidebar.header('Input Features')

# Sale Date
saledate = st.sidebar.date_input('Sale Date', datetime.today())

# Important features in the required order
fi_secondary_desc = st.sidebar.text_input('fiSecondaryDesc', '6E')
model_id = st.sidebar.number_input('ModelID', min_value=0, value=1000)
product_size = st.sidebar.selectbox('ProductSize', ['Small', 'Medium', 'Large'], index=1)
year_made = st.sidebar.number_input('YearMade', min_value=1900, max_value=2023, value=2000)
enclosure = st.sidebar.selectbox('Enclosure', ['EROPS w AC', 'OROPS'], index=0)
fi_base_model = st.sidebar.text_input('fiBaseModel', 'PC120')
fi_model_descriptor = st.sidebar.text_input('fiModelDescriptor', '6E')
fi_model_desc = st.sidebar.text_input('fiModelDesc', 'PC120-6E')
forks = st.sidebar.selectbox('Forks', ['None or Unspecified', 'Yes'], index=0)
coupler_system = st.sidebar.selectbox('Coupler_System', ['None or Unspecified', 'Yes'], index=0)
machine_id = st.sidebar.number_input('MachineID', min_value=0, value=500000)
hydraulics_flow_is_missing = st.sidebar.checkbox('Hydraulics_Flow_is_missing', value=False)
tire_size = st.sidebar.text_input('Tire_Size', '23.5')
fi_product_class_desc = st.sidebar.text_input('fiProductClassDesc', 'Hydraulic Excavator')
sales_id = st.sidebar.number_input('SalesID', min_value=0, value=1000000)
stick_length_is_missing = st.sidebar.checkbox('Stick_Length_is_missing', value=False)
grouser_tracks_is_missing = st.sidebar.checkbox('Grouser_Tracks_is_missing', value=False)
hydraulics_flow = st.sidebar.selectbox('Hydraulics_Flow', ['Standard', 'High'], index=0)
product_size_is_missing = st.sidebar.checkbox('ProductSize_is_missing', value=False)
ripper = st.sidebar.selectbox('Ripper', ['None or Unspecified', 'Yes'], index=0)

input_data = {
    'fiSecondaryDesc': fi_secondary_desc,
    'ModelID': model_id,
    'ProductSize': product_size,
    'YearMade': year_made,
    'Enclosure': enclosure,
    'fiBaseModel': fi_base_model,
    'fiModelDescriptor': fi_model_descriptor,
    'fiModelDesc': fi_model_desc,
    'Forks': forks,
    'Coupler_System': coupler_system,
    'MachineID': machine_id,
    'Hydraulics_Flow_is_missing': hydraulics_flow_is_missing,
    'Tire_Size': tire_size,
    'fiProductClassDesc': fi_product_class_desc,
    'SalesID': sales_id,
    'Stick_Length_is_missing': stick_length_is_missing,
    'Grouser_Tracks_is_missing': grouser_tracks_is_missing,
    'Hydraulics_Flow': hydraulics_flow,
    'ProductSize_is_missing': product_size_is_missing,
    'Ripper': ripper,
    'saledate': saledate
}

# Preprocess the input data
processed_data = preprocess_input(input_data)

# Ensure the columns are in the correct order
processed_data = processed_data[['fiSecondaryDesc', 'ModelID', 'ProductSize', 'YearMade', 'Enclosure', 'fiBaseModel', 'fiModelDescriptor', 'fiModelDesc', 'Forks', 'Coupler_System', 'MachineID', 'Hydraulics_Flow_is_missing', 'Tire_Size', 'fiProductClassDesc', 'SalesID', 'Stick_Length_is_missing', 'Grouser_Tracks_is_missing', 'Hydraulics_Flow', 'ProductSize_is_missing', 'Ripper']]

# Make prediction
if st.sidebar.button('Predict'):
    prediction = model.predict(processed_data)
    st.success(f'Predicted Bulldozer Price: ${prediction[0]:.2f}')