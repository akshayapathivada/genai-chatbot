# Gemini AI Chatbot

This project implements a Gemini AI Chatbot using Streamlit, Google Generative AI, and various Python libraries. The chatbot supports different functionalities including text-only input, image and text input, chat history with embeddings, and invoice processing.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Features](#features)
  - [Text Chat](#text-chat)
  - [Image and Text Chat](#image-and-text-chat)
  - [Chat History with Embeddings](#chat-history-with-embeddings)
  - [Invoice Processing](#invoice-processing)
- [License](#license)

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/gemini-ai-chatbot.git
    cd gemini-ai-chatbot
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Set up environment variables:
    - Create a `.env` file in the root directory of the project.
    - Add your Google API key to the `.env` file:
      ```env
      GOOGLE_API_KEY=your_google_api_key
      ```

## Usage

Run the Streamlit app:

```bash
streamlit run app.py


.
├── app.py
├── vision.py
├── qachat.py
├── invoice.py
├── requirements.txt
└── README.md

app.py: Handles text-only chat functionality.
vision.py: Supports both image and text input using the Gemini Flash model.
qachat.py: Manages chat history using embeddings.
invoice.py: Processes invoices which can include images.
Features
Text Chat
Handled by app.py, this feature allows users to interact with the chatbot using text input. It uses the Gemini AI model to generate responses based on the provided text.

Image and Text Chat
Implemented in vision.py, this feature supports both text and image inputs. The Gemini Flash model processes the inputs and generates responses that consider both the image and text.

Chat History with Embeddings
Implemented in qachat.py, this feature maintains the chat history using embeddings, allowing the chatbot to refer to previous interactions and provide contextually relevant responses.

Invoice Processing
Handled by invoice.py, this feature processes images of invoices, extracting relevant information and answering queries related to the invoice.
