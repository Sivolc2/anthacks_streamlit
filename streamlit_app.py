# streamlit_app.py

import os
import streamlit as st
from llm_functions import *
from audio_functions import generate_audio

def main():
    # Set a title
    st.title("My LangChain App")

    # Display environment variable information
    st.write(
        "Has environment variables been set:",
        os.environ["ANTHROPIC_API_KEY"] == st.secrets["ANTHROPIC_API_KEY"],
    )

    # Select between the translation, chat, and audio pages
    page = st.sidebar.selectbox("Choose a page:", ["Translation", "Chat", "Audio"])

    if page == "Translation":
        translation_page()
    elif page == "Chat":
        chat_page()
    elif page == "Audio":
        audio_page()


def audio_page():
    # Generate an audio signal
    audio_signal, sample_rate = generate_audio()

    # Display an audio player
    st.audio(audio_signal, format='audio/wav', start_time=0, sample_rate=sample_rate)


if __name__ == "__main__":
    main()
