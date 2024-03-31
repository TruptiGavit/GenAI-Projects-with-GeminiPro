from dotenv import load_dotenv
load_dotenv()##loading environment variavles


import streamlit as st
import os
import pathlib
import textwrap
from PIL import Image

import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

##load gemini pro and get response
def get_gemini_response(input,image):
    model = genai.GenerativeModel('gemini-pro-vision')
    if input!="":
       response = model.generate_content([input,image])
    else:
       response = model.generate_content(image)
    return response.text


def main():
##streamlit app setup


    st.header("Trupti's First Gemini Application")
    input=st.text_input("Input Prompt: ",key="input")

    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    image=""   
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image.", use_column_width=True)


    submit=st.button("Tell me about the image")


    ##when submit clicked
    if submit:
        response=get_gemini_response(input,image)
        st.subheader("The Response is")
        st.write(response)


if __name__ == "__main__":
    main()