# Custom GPT Chat Application

A simple chat application built with Streamlit and Groq's OpenAI-compatible API that provides a GPT-like experience.

## Setup

1. Clone this repository
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Create a `.env` file in the root directory and add your Groq API key:
   ```
   GROQ_API_KEY=your_groq_api_key_here
   ```
   You can get your API key from the [Groq Console](https://console.groq.com/keys)

## Running the Application

To run the application, use the following command:
```bash
streamlit run app.py
```

The application will open in your default web browser at `http://localhost:8501`

## Features

- Clean and modern chat interface
- Real-time responses using Groq LLMs
- Chat history persistence during the session
- Error handling for API issues
- Responsive design

## Requirements

- Python 3.7+
- Streamlit
- OpenAI Python SDK
- python-dotenv 