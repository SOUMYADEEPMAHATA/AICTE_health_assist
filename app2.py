import streamlit as st
from transformers import pipeline
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import torch

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')


chatbot = pipeline(
                       "text-generation", 
    model="meta-llama/Llama-3.2-1B-Instruct",
    #tokenizer="google-t5/t5-small",
    use_fast=False,
    torch_dtype=torch.bfloat16,
    device="cuda",) # Force using the SentencePiece tokenizer instead of tiktoken)

def preprocess_input(user_input):
    stop_words = set(stopwords.words('english'))
    words = word_tokenize(user_input)
    filtered_words = [word for word in words if word.lower() not in stop_words]
    return ' '.join(filtered_words)

def healthcare_chatbot(user_input):
    #user_input = preprocess_input(user_input)
    if 'sneeze' in user_input or 'sneezing' in user_input:
        return " Freequent sneezing may indicate allergies or cold"
    elif "symptom" in user_input:
        "Consult doctor please."
    elif "appointment" in user_input:
        return "Would you like to schedule an appointment"
    elif "medication" in user_input:
        return "It's important to take your prescribed medication regularly. If you have concerns concsult your doctor please."
    else:
        context = """
        Common healthcare realted scenarios include symptoms of cold, flu, and allergies, along with medication guidance and appointment scheduling."""
        #response = chatbot(context)
        response = chatbot([{"role":"system", "content": "You are a Healthcare assistant."},
                            {"role": "user", "content" : user_input}],  
                            max_new_tokens=256)
        return response[0]['generated_text'][2]["content"] #['generated_text']
    
def main():
    st.title("Healthcare Assistant")
    user_input = st.text_input("Hello, How can I assist you today?")
    if st.button('Submit'):
        if user_input:
            st.write('user: ', user_input)
            response = healthcare_chatbot(user_input=user_input)
            st.write("Healthcare Assistant: ", response)
        else:
            st.write("Please enter your query. ")

if __name__ == "__main__":
    main()