# streamlit_app.py

# Import necessary libraries
import streamlit as st
import pandas as pd
import numpy as np

# Define your Streamlit application
def main():

    # Set a title
    st.title("My Streamlit App")

    # Write some text
    st.write("Welcome to my application. Please interact with it from the sidebar.")

    # Create a sidebar with a selectbox for user selection
    st.sidebar.title('Interactions')
    user_choice = st.sidebar.selectbox("Choose your action", ["Display text", "Display DataFrame"])

    # Based on the user choice, display the corresponding information
    if user_choice == "Display text":
        st.write("You selected to display text.")
    elif user_choice == "Display DataFrame":
        st.write("You selected to display a DataFrame. Here it is:")
        df = pd.DataFrame({
        'first column': list(range(1, 101)),
        'second column': np.random.randn(100).tolist()
        })
        st.write(df)

if __name__ == "__main__":
    main()
