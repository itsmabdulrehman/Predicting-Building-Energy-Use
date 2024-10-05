import streamlit as st
import numpy as np
from predict_page import show_prediction_page
from explore_page import show_explore_page
from PIL import Image

img = Image.open(r"Files/icon.jpg")
st.set_page_config(page_title='Machine Learning Model', page_icon=img)

st.sidebar.image(img, use_column_width=True)
st.sidebar.markdown("""---""")
st.sidebar.write("## Predicting Energy use in buildings")

option = ["Predict", "Explore"]
default_index = 0
page = st.sidebar.selectbox("Predict or Explore", options=option, help="Switch between Predict and Explore Page", placeholder="Choose an option",disabled=False, index=default_index)

hide_menu_style = """
    <style>
        .reportview-container {
            margin-top: -2em;
        }
        #MainMenu {visibility: hidden;}
        .stDeployButton {display:none;}
        footer {visibility: hidden;}
        #stDecoration {display:none;}
    </style>
    """
st.markdown(hide_menu_style, unsafe_allow_html=True)

if page == "Predict":
    show_prediction_page()
else:
    show_explore_page()
