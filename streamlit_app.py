import streamlit as st
from test import show_page

st.set_page_config(layout="wide")



st.markdown(page_bg_img, unsafe_allow_html=True)

show_page()