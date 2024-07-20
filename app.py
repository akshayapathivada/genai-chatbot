from dotenv import load_dotenv
import streamlit as st
import os
import textwrap
import google.generativeai as genai

def to_markdown(text):
    text = text.replace('•', '  *')
    return textwrap.indent(text, '> ', predicate=lambda _: True)

# Load environment variables from .env file
load_dotenv()

# Retrieve the API key from the environment variables
api_key = os.getenv("GOOGLE_API_KEY")

# Print the API key for debugging
print("API Key:", api_key)

# Check if the API key is loaded correctly
if not api_key:
    st.error("GOOGLE_API_KEY not found in environment variables.")
else:
    # Configure the Google Generative AI with the API key
    genai.configure(api_key="AIzaSyBIRctJ23ZDvn8p-XMm28QSbGHJN4ItgJk")


    ## Function to load OpenAI model and get responses
    def get_gemini_response(question):
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(question)
        return response.text

    ## Initialize our Streamlit app
    st.set_page_config(page_title="Q&A Demo")

    st.header("Gemini Application")

    input = st.text_input("Input: ", key="input")

    submit = st.button("Ask the question")

    ## If ask button is clicked
    if submit:
        response = get_gemini_response(input)
        st.subheader("The Response is")
        st.write(to_markdown(response))
