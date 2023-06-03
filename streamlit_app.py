# streamlit_app.py
import streamlit as st
from llm_functions import *

## Streamlit envvars
st.write(
    "Has environment variables been set:",
    os.environ["ANTHROPIC_API_KEY"] == st.secrets["ANTHROPIC_API_KEY"],
)

## Utils
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
