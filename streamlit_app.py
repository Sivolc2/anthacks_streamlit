# streamlit_app.py

# Import necessary libraries
import streamlit as st
from langchain.chat_models import ChatAnthropic
from langchain.schema import HumanMessage
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler


def main():

    # Set a title
    st.title("My LangChain Translation App")

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
        st.write(f"The translated sentence is: {response[0].content}")

        # Uncomment the following lines if you want to use streaming and verbosity
        # chat = ChatAnthropic(streaming=True, verbose=True, callback_manager=CallbackManager([StreamingStdOutCallbackHandler()]))
        # response = chat(messages)

if __name__ == "__main__":
    main()
