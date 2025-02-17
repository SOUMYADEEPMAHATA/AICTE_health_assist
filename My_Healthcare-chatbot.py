import streamlit as st
from transformers import pipeline
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import torch
from utils.llm_code import chatbot

    
def main():
    st.title("Healthcare Assistant")
    user_input = st.text_input("Hello, How can I assist you today?")
    if st.button('Submit'):
        if user_input:
            st.write('user: ', user_input)
            response = chatbot(user_input=user_input)
            st.write("Mahata's Healthcare Assistant: ", response)
        else:
            st.write("Please enter your query. ")

if __name__ == "__main__":
    main()