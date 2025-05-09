import streamlit as st
import google.generativeai as genai
from config import BASE_PROMPT, GEMINI_API_KEY

# Configure Gemini API
genai.configure(api_key=GEMINI_API_KEY)

def chat_bot():
    # Initialize session state variables
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": "Hi! How may I help you?"}]
    if "chat" not in st.session_state:
        model = genai.GenerativeModel(
            model_name="models/gemini-1.5-flash-latest",
            system_instruction=BASE_PROMPT
        )
        st.session_state.chat = model.start_chat(history=[])

    # Display previous messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    # User input
    if prompt := st.chat_input("Type your message..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.write(prompt)

        # Generate assistant response
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                try:
                    response = st.session_state.chat.send_message(prompt).text
                except Exception as e:
                    response = f"Error: {str(e)}"
                st.write(response)

        st.session_state.messages.append({"role": "assistant", "content": response})