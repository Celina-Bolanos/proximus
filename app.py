import streamlit as st
#from utils.functions import select_file
import pandas as pd


#image_path = "./utils/house_header.jpg"
#st.image(image_path, caption=None, use_container_width=True)

st.title("Proximus Phishing Test App")
st.write("Welcome!")

#st.write("Menu")
menu_selection = st.selectbox("Menu", ["Make a selection", "Upload new email list", "See current campaigns"])

if menu_selection == "Upload new email list":
    file = st.file_uploader(label='Upload your emails file', type=['json'])
    # target = pd.read_json(file)
    st.write(print(type(file)))
  


#if st.button("Start"):
#    select_file()
