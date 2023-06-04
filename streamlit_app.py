# streamlit_app.py
import streamlit as st
from llm_functions import *
from audio_functions import st_audiorec  # Ensure this is available

## Streamlit envvars
st.write(
    "ANTHROPIC_API_KEY",
    os.environ["ANTHROPIC_API_KEY"] == st.secrets["ANTHROPIC_API_KEY"],
)
st.write(
    'OPENAI_API_KEY', os.environ["OPENAI_API_KEY"] == st.secrets["OPENAI_API_KEY"],
)
st.write(
    'ELEVENLABS_API_KEY', os.environ["ELEVENLABS_API_KEY"] == st.secrets["ELEVENLABS_API_KEY"]
)


## Utils
def main():
    # Set a title
    st.title("My LangChain App")

    # Select between the translation, chat, and audio recording pages
    page = st.sidebar.selectbox("Choose a page:", ["Translation", "Chat", "Audio Recording"])

    if page == "Translation":
        translation_page()
    elif page == "Chat":
        chat_page()
    elif page == "Audio Recording":
        audio_recording_page()


def audio_recording_page():
    wav_audio_data = st_audiorec()

    if wav_audio_data is not None:
        st.audio(wav_audio_data, format='audio/wav')

if __name__ == "__main__":
    main()
