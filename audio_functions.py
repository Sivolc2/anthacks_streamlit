# audio_functions.py

import numpy as np
import streamlit as st

def generate_audio():
    # Sample rate 44100 Hz
    sample_rate = 44100  
    seconds = 2  # Note duration of 2 seconds
    frequency_la = 440  # Our played note will be 440 Hz

    # Generate array with seconds*sample_rate steps, ranging between 0 and seconds
    t = np.linspace(0, seconds, seconds * sample_rate, False)

    # Generate a 440 Hz sine wave
    note_la = np.sin(frequency_la * t * 2 * np.pi)

    return note_la, sample_rate

def autoplay_audio(audio_bytes):
    b64 = base64.b64encode(audio_bytes).decode()
    md = f"""
        <audio autoplay>
        <source src="data:audio/ogg;base64,{b64}" type="audio/ogg">
        </audio>
        """
    st.markdown(md, unsafe_allow_html=True)
