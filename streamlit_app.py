# streamlit_app.py

# Import necessary libraries
import streamlit as st
from langchain.chat_models import ChatAnthropic
from langchain.schema import HumanMessage
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from anthropic import AnthropicClient

## Get Key
st.write(
    "Has environment variables been set:",
    os.environ["ANTHROPIC_API_KEY"] == st.secrets["ANTHROPIC_API_KEY"],
)
anthropic_client = anthropic.Client(api_key=os.getenv("ANTHROPIC_API_KEY"))

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
        st.write(f"The translated sentence is: {response[0].content}")


def chat_page():
    anthropic_client = AnthropicClient(api_key=os.environ["ANTHROPIC_API_KEY"])
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


def main():
    # Set a title
    st.title("My LangChain App")

    # Select between the translation and chat pages
    page = st.sidebar.selectbox("Choose a page:", ["Translation", "Chat"])

    if page == "Translation":
        translation_page()
    elif page == "Chat":
        chat_page()


if __name__ == "__main__":
    main()
