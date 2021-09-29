# import statements
import streamlit as st
from PIL import Image
import numpy as np
import pandas as pd
import os

# adding title in the app
st.title('Food Classification and calorie count')
# load Image
def load_image(uploaded_file):
    img = Image.open(uploaded_file)
    return img
# Adding upload file option in the web
uploaded_file = st.file_uploader("Pick a Photo", type=['pnj','jpeg','jpg'])
if uploaded_file is not None:
    file_details = {"FileName":uploaded_file.name,"FileType":uploaded_file.type,"FileSize":uploaded_file.size}
    # st.write(file_details)
    st.image(load_image(uploaded_file),width=220)
    save_image_path = './Upload_Images/' + uploaded_file.name
    with open(save_image_path, "wb") as f:
        f.write(uploaded_file.getbuffer())