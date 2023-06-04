#llm_functions.py
import os
import requests
import base64
from pathlib import Path
import numpy as np

# Import necessary libraries
import streamlit as st
from langchain.chat_models import ChatAnthropic
from langchain.schema import HumanMessage
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from elevenlabs import generate as generate_audio, set_api_key as elevenlabs_set_api_key
from whisper import WhisperModel, WhisperArgs, Transcriber

from audio_functions import autoplay_audio

## Get Key
elevenlabs_set_api_key(os.getenv("ELEVENLABS_API_KEY"))

def translation_page():
    # Ask the user for a sentence to translate
    user_sentence = st.text_input("Please enter a sentence to translate from English to French:")

    # Only attempt to translate when the user has entered a sentence
    if user_sentence:
        chat = ChatAnthropic()

        messages = [
            HumanMessage(content=f"Translate this sentence from English to French. {user_sentence}")
        ]
        response = chat(messages)

        # Display the translation
        st.write(f"The translated sentence is: {response.content}")

def chat_page():
    import anthropic
    anthropic_client = anthropic.Client(api_key=os.getenv("ANTHROPIC_API_KEY"))

    context = ""
    user_inp = st.text_input("You: ")

    if user_inp:
        current_inp = anthropic.HUMAN_PROMPT + user_inp + anthropic.AI_PROMPT
        context += current_inp

        prompt = context

        completion = anthropic_client.completion(
            prompt=prompt, model="claude-v1.3-100k", max_tokens_to_sample=1000
        )["completion"]

        context += completion

        # Display the response from the model
        st.write("Anthropic: " + completion)

        # Generate an audio file with the response and play it
        audio = generate_audio(
            text=completion,
            voice="Arnold",
            model='eleven_multilingual_v1'
        )
        audio_base64 = base64.b64encode(audio).decode('utf-8')
        audio_tag = f'<audio autoplay src="data:audio/ogg;base64,{audio_base64}">'
        st.markdown(audio_tag, unsafe_allow_html=True)

class MediaManager:
    """A class to act as a primary interface to manage media objects and related data"""

    def __init__(self, media_dir: Path = MEDIA_DIR):
        self.media_dir = media_dir
        # Create the media directory if it doesn't exist
        self.media_dir.mkdir(exist_ok=True, parents=True)

    def _transcribe(self, audio_path: str, whisper_model: str):
        """Transcribe the audio file using whisper"""

        # Load whisper model
        model = whisper.load_model(whisper_model)

        # Transcribe the audio file
        transcript = model.transcribe(audio_path)

        return transcript
