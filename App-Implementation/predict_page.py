import streamlit as st
import pandas as pd
import numpy as np
import joblib
import pickle
from sklearn.preprocessing import MinMaxScaler

def load_data():
    data = pd.read_csv(r'Files/Building Energy Efficiency.csv')
    return data

def load_model():
    model = joblib.load(r'Files/singleloadmodel.pkl')
    return model

def make_prediction(model, input_data):
    MinMax = MinMaxScaler(feature_range= (0,1))

    df = load_data()
    X_train = df[['Relative Compactness', 'Surface Area', 'Wall Area', 'Roof Area', 'Overall Height', 'Orientation', 'Glazing Area', 'Glazing Area Distribution']]

    X_train = MinMax.fit_transform(X_train)
    input_data = MinMax.transform(input_data)
    prediction = model.predict(input_data)

    return prediction

model = load_model()

def convert_distributions(Distribution):
    if Distribution == 'Uniform':
        Distribution = 1
        return Distribution
    if Distribution == 'North':
        Distribution = 2
        return Distribution
    if Distribution == 'East':
        Distribution = 3
        return Distribution
    if Distribution == 'South':
        Distribution = 4
        return Distribution
    if Distribution == 'West':
        Distribution = 5
        return Distribution
    
def convert_orientations(Orientation):
    if Orientation == 'North':
        Orientation = 2
        return Orientation
    if Orientation == 'East':
        Orientation = 3
        return Orientation
    if Orientation == 'South':
        Orientation = 4
        return Orientation
    if Orientation == 'West':
        Orientation = 5
        return Orientation
                

def show_prediction_page():
    input_data = []
    st.title("Predicting Energy Use in Buildings")
    st.divider()
    st.write("""### Enter Physical Parameters:-""")

    with st.form("my_form"):
        st.write("""###### Please enter the following information to predict the energy load of a building:""")
        Relative_Compactness = st.slider("Relative Compactness:", 0.65, 0.95, 0.65, step=0.05)
        Surface_Area = st.number_input("Surface Area:", 500, 850, step=1)
        Wall_Area = st.number_input("Wall Area:", 250, 425, step=1)
        Roof_Area = st.number_input("Roof Area:", 120, 220, step=1)
        Overall_Height = st.number_input("Overall Height:", 3.5, 7.0, step=0.1)
        Orientation = st.selectbox('Pick a Orientation:', ['North','East','West','South'], help="Choose an Orientation", placeholder="Choose an Orientation...", disabled=False, index=None)
        Orientation = convert_orientations(Orientation)
        Glazing_Area_percent_of_floor_area = st.slider("Glazing Area (% of floor area):", 0, 40, 0, step=10, format="%d%%")
        Glazing_Area_Distribution = st.selectbox('Pick a Glazing Area Distribution:', ['Uniform','North','East','West','South'], help="Choose a Distribution", placeholder="Choose a Distribution...", disabled=False, index=None)
        Glazing_Area_Distribution = convert_distributions(Glazing_Area_Distribution)
        predict_button = st.form_submit_button('Predict')
    
    if predict_button:
        if Orientation == None or Glazing_Area_Distribution == None:
            st.warning("Please choose the options to calculate the Total Energy Load of the Building")
        else:
            input_data = [[Relative_Compactness, Surface_Area, Wall_Area, Roof_Area, Overall_Height, Orientation, Glazing_Area_percent_of_floor_area, Glazing_Area_Distribution]]
            prediction_result = make_prediction(model, input_data)

            #st.subheader(f"Total Energy Load Prediction: {(prediction_result[0]):.2f} kW" )
            st.metric(label="## Total Energy Load Prediction:", value=f"{(prediction_result[0]):.2f} kW")
