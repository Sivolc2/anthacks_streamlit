import os
import requests

# Import necessary libraries
import streamlit as st
from langchain.chat_models import ChatAnthropic
from langchain.schema import HumanMessage
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
import anthropic
from elevenlabs import generate as generate_audio, set_api_key as elevenlabs_set_api_key

elevenlabs_set_api_key(os.getenv("ELEVENLABS_API_KEY"))

## Get Key

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
    anthropic_client = anthropic.Client(api_key=os.getenv("ANTHROPIC_API_KEY"))

    anthropic = ChatAnthropic()

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
        st.audio(audio, format='audio/ogg')

# def whisper_api():
    
#     OPENAI_API_KEY = os.environ['OPENAI_API_KEY']

#     url = 'https://api.openai.com/v1/audio/transcriptions'
#     headers = {'Authorization': f'Bearer {OPENAI_API_KEY}'}
#     files = {'file': open(file_path, 'rb'),
#             'model': (None, 'whisper-1')
#     }
#     response = requests.post(url, headers=headers, files=files)
#     output_path = os.path.join(folder_path, os.path.splitext(os.path.basename(file_path))[0] + '.' + output_format)
#     with open(output_path, 'w') as f:
#         f.write(response.content.decode('utf-8'))


