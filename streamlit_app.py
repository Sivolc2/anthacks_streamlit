# streamlit_app.py
import streamlit as st
from llm_functions import MediaManager
from st_custom_components import st_audiorec
from whisper import WhisperArgs
import os

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

WHISPER_DEFAULT_SETTINGS = {
    "whisper_model": "base",
    "temperature": 0.0,
    "temperature_increment_on_fallback": 0.2,
    "no_speech_threshold": 0.6,
    "logprob_threshold": -1.0,
    "compression_ratio_threshold": 2.4,
    "condition_on_previous_text": True,
    "verbose": False,
    "task": "transcribe",
}

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
        # Save the recorded audio to a .wav file
        audio_path = 'path_to_your_audio_file.wav'
        with open(audio_path, 'wb') as f:
            f.write(wav_audio_data)

        # Define whisper model and arguments
        whisper_model = WHISPER_DEFAULT_SETTINGS['whisper_model']
        whisper_args = WhisperArgs(
            temperature=0.8,
            temperature_increment_on_fallback=0.05,
            max_tokens=None,
            sample=True,
        )

        # Initialize the MediaManager class with the whisper model and arguments
        media_manager = MediaManager(whisper_model, whisper_args)

        # Transcribe the audio
        transcript = media_manager._transcribe(audio_path)
        st.write(transcript)

if __name__ == "__main__":
    main()
