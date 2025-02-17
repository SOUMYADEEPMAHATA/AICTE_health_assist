
from langchain_ollama import OllamaLLM
from langchain.prompts import PromptTemplate

# Define llm
llm = OllamaLLM(model="Deepseek-R1-medical:latest")          #"deepseek-r1:1.5b")

# Define the prompt
prompt = """
1. Use the following pieces of context to answer the question at the end.
2. If you don't know the answer, just say that "I don't know" but don't make up an answer on your own.\n
Question: {input}
Helpful Answer:"""

QA_CHAIN_PROMPT = PromptTemplate.from_template(prompt)

chain = QA_CHAIN_PROMPT | llm

def chatbot(user_input):
    response = chain.invoke({"input":user_input})
    #print(response)
    str_idx = response.find("/think>") + 7
    # print("Response:")
    # print(response[str_idx:].strip())
    return(response[str_idx:].strip())

    
#chatbot("What is Vision Language Model?")