st.set_page_config(page_title="Bangla OCR Tool", layout="centered")

st.title("📄 Bangla Ejar OCR Tool")
st.write("👉 Upload → OCR → Auto Fix → Download")

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

    new_text = text
new_text = new_text.replace("আমার","বাদীর")
new_text = new_text.replace("আমাকে","বাদীকে")
new_text = new_text.replace("আমাদের","বাদীদের")
new_text = new_text.replace("আমি","বাদী")

    st.write("Final Text:")
    st.text_area("", new_text)

    st.download_button("Download", new_text)
