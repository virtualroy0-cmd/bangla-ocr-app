import streamlit as st
from PIL import Image
import pytesseract
from pdf2image import convert_from_bytes

st.set_page_config(page_title="Bangla OCR Tool", layout="centered")

st.title("📄 Bangla Ejar OCR Tool")
st.write("👉 Upload → OCR → Auto Fix → Download")

uploaded_file = st.file_uploader("Upload Image or PDF", type=["png","jpg","jpeg","pdf"])

if uploaded_file is not None:

    if uploaded_file.type == "application/pdf":
        images = convert_from_bytes(uploaded_file.read())
        image = images[0]
    else:
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
    new_text = new_text.replace("করতেছি","করেন")
    new_text = new_text.replace("পারি","পারেন")
    new_text = new_text.replace("করি","করেন")

    st.write("Final Text:")
    st.text_area("", new_text)

    st.download_button("Download", new_text)
