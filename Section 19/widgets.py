import streamlit as st # pyright: ignore[reportMissingImports]
import pandas as pd
import numpy as np

st.title("Streamlit Widgets Demo")

name=st.text_input("Enter your name:")

age=st.slider("Slect your age",0,100,25)
if name:
    st.write(f"Hello, {name}!")
st.write(f"Your name is {name} and you are {age} years old.")

options = ["Python", "JavaScript", "C++", "Java"]
favorite_language = st.selectbox("Select your favorite programming language:", options)
st.write(f"Your favorite programming language is {favorite_language}.")

data = {
    "Name": ["Inder", "Shyam", "Aman", "Rohit"],
    "Age": [25, 30, 22, 28],
    "City":["Gurugram", "Delhi", "Noida", "Mumbai"]
}

df = pd.DataFrame(data)
st.write("Here is the data frame:")
st.write(df)

upload_file=st.file_uploader("Upload a CSV file", type=["csv"])
if upload_file is not None:
    uploaded_df = pd.read_csv(upload_file)
    st.write("Uploaded CSV file:")
    st.write(uploaded_df)