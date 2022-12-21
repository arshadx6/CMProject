import streamlit as st
from PIL import Image
st.write("Hello from Streamlitssss")
st.title(" Welcome to the smart blood report generator ")
image = Image.open('sunrise.svg')
st.image(image, caption='Sunrise by the mountains')
