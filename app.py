import streamlit as st
from groq import Groq
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Configure the Groq API
GROQ_API_KEY = os.getenv('GROQ_API_KEY')
client = Groq(api_key=GROQ_API_KEY)

# Set your Groq model name (e.g., llama3-70b-8192 or mixtral-8x7b-32768)
MODEL_NAME = "llama3-70b-8192"

# Set page config
st.set_page_config(
    page_title="Custom GPT Chat",
    page_icon="🤖",
    layout="centered"
)

# Custom CSS
st.markdown("""
    <style>
    .stTextInput>div>div>input {
        background-color: #f0f2f6;
        color: black !important;
    }
    .chat-message {
        padding: 1.5rem;
        border-radius: 1rem;
        margin-bottom: 1.5rem;
        display: flex;
        flex-direction: column;
        color: black !important;
        background: #fff;
        box-shadow: 0 2px 12px 0 rgba(0,0,0,0.08);
        border: 1px solid #e0e0e0;
    }
    .chat-message.user {
        background-color: #e3e8f0;
        color: black !important;
        align-self: flex-end;
        border: 1px solid #bfc8d6;
    }
    .chat-message.assistant {
        background-color: #fff;
        color: black !important;
        align-self: flex-start;
        border: 1px solid #e0e0e0;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Title
st.title("🤖 Project Suggestion Agent")
# Animated 'Developed by Deepak' text
st.markdown("""
    <div class="typewriter">
      <span>Developed by Deepak kumar</span>
    </div>
    <style>
    .typewriter span {
      display: inline-block;
      overflow: hidden;
      border-right: .15em solid orange;
      white-space: nowrap;
      margin: 0 auto;
      letter-spacing: .15em;
      animation:
        typing 2.5s steps(22, end),
        blink-caret .75s step-end infinite;
      font-size: 1.2rem;
      color: #ffb347;
      font-family: 'Fira Mono', 'Consolas', monospace;
    }
    @keyframes typing {
      from { width: 0 }
      to { width: 100% }
    }
    @keyframes blink-caret {
      from, to { border-color: transparent }
      50% { border-color: orange; }
    }
    </style>
""", unsafe_allow_html=True)
st.markdown("---")

# Display chat messages
for message in st.session_state.messages:
    if message["role"] == "system":
        continue  # Skip displaying the system prompt
    with st.container():
        st.markdown(f"""
            <div class="chat-message {message['role']}">
                <div>{message['content']}</div>
            </div>
        """, unsafe_allow_html=True)

def send_message():
    user_input = st.session_state.user_input
    if user_input:
        # Add system prompt if it's the first message
        if not st.session_state.messages:
            st.session_state.messages.append({
                "role": "system",
                "content": "You are Deepak's helpful AI assistant. You're an expert in providing projects based on the tech stack they mention. So, you will answer all the questions related to projects based on the tech stack they mention. If they didn't ask about projects, you will say that you are an Project Suggestion Agent developed by Deepak."
            })
        st.session_state.messages.append({"role": "user", "content": user_input})
        # Prepare messages for Groq API
        messages = []
        for msg in st.session_state.messages:
            messages.append({"role": msg["role"], "content": msg["content"]})
        try:
            response = client.chat.completions.create(
                model=MODEL_NAME,
                messages=messages,
                temperature=0.7,
                max_tokens=1024
            )
            ai_response = response.choices[0].message.content.strip()
            st.session_state.messages.append({"role": "assistant", "content": ai_response})
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
        st.session_state.user_input = ""  # This is now safe

# Chat input
st.text_input(
    "Enter Tech Stack, Deepak is here to suggest projects based on the tech stack",
    key="user_input",
    on_change=send_message
) 