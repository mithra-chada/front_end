import streamlit as st
from PIL import Image
from image_captioning import generate_caption

st.title("Image Captioning")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    st.write("")
    st.write("Generating caption...")
    caption = generate_caption(image)
    st.write(caption)
