import streamlit as st
from PIL import Image
import pytesseract

st.title("Bangla OCR Auto Replace App")

uploaded_file = st.file_uploader("Upload Image", type=["png","jpg","jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image)

    text = pytesseract.image_to_string(image, lang='ben')

    st.write("OCR Text:")
    st.text_area("", text)

    new_text = text.replace("আমার","বাদীর").replace("আমাকে","বাদীকে")

    st.write("Final Text:")
    st.text_area("", new_text)

    st.download_button("Download", new_text)
