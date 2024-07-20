from dotenv import load_dotenv
import streamlit as st
import os
from PIL import Image
import google.generativeai as genai

# Load environment variables from .env file
load_dotenv()

# Retrieve the API key from the environment variables
api_key = os.getenv("GOOGLE_API_KEY")

# Check if the API key is loaded correctly
if not api_key:
    st.error("GOOGLE_API_KEY not found in environment variables.")
else:
    # Configure the Google Generative AI with the API key
    genai.configure(api_key=api_key)

    ## Function to load Gemini model and get responses
    def get_gemini_response(input, image):
        try:
            model = genai.GenerativeModel('gemini-1.5-flash')
            if input and image:
                response = model.generate_content([input, image])
            elif input:
                response = model.generate_content(input)
            elif image:
                response = model.generate_content(image)
            else:
                response = "No input provided."
            return response.text
        except Exception as e:
            st.error(f"An error occurred: {e}")
            return "An error occurred while processing the request."

    ## Initialize our Streamlit app
    st.set_page_config(page_title="Gemini Image Demo")

    st.header("Gemini Application")
    input = st.text_input("Input Prompt: ", key="input")
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    image = None
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image.", use_column_width=True)

    submit = st.button("Tell me about the image")

    ## If ask button is clicked
    if submit:
        response = get_gemini_response(input, image)
        st.subheader("The Response is")
        st.write(response)
