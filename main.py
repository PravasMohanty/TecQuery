import os
import streamlit as st
from constants import google_api

# LangChain Imports
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SimpleSequentialChain , SequentialChain
from langchain.memory import ConversationBufferMemory
from langchain_google_genai import ChatGoogleGenerativeAI

# ===============================
# Environment & API Configuration
# ===============================
os.environ["GOOGLE_API_KEY"] = google_api

# ===============================
# Memory for Conversation Context
# ===============================
# Set input_key='input_text' to match prompt inputs
topic_memory = ConversationBufferMemory(input_key='input_text', memory_key='chat_history')
example_memory = ConversationBufferMemory(input_key='input_text', memory_key='chat_history')

# ===============================
# Initialize LLM Model
# ===============================
llm = ChatGoogleGenerativeAI(model="models/gemini-1.5-flash-latest")

# ===============================
# Prompt Templates
# ===============================
first_input_prompt = PromptTemplate(
    input_variables=['input_text'],
    template="""
# **Role**
You are an expert in technology and coding concepts.

# **Objective**
Provide a clear and concise description of the given input content.

# **Content**
{input_text}

# **Instructions**
1. Ensure relevance to technical and coding subjects.
2. Avoid irrelevant or unnecessary data.
3. Keep the response concise and focused.
"""
)

second_input_prompt = PromptTemplate(
    input_variables=['input_text'],
    template="""
Provide a simple example or illustration of {input_text} 
that helps the reader understand the concept easily.
"""
)

# ===============================
# LLM Chains
# ===============================
chain1 = LLMChain(
    llm=llm,
    prompt=first_input_prompt,
    verbose=True,
    output_key='info',
    memory=topic_memory
)

chain2 = LLMChain(
    llm=llm,
    prompt=second_input_prompt,
    verbose=True,
    output_key='example',
    memory=example_memory
)

# Sequential chain combining both steps
parent_chain = SimpleSequentialChain(chains=[chain1, chain2], verbose=True)
seq_parent_chain = SequentialChain(chains=[chain1, chain2],input_variables=['input_text'],output_variables=['info','example'], verbose=True)

# ===============================
# Streamlit UI
# ===============================
st.title("LangChain Demo with Google GEMINI API - Coding Version")

input_text = st.text_input("Enter a coding-based topic:")

if input_text:
    response = parent_chain.run(input_text)
    response_seq = seq_parent_chain({'input_text': input_text})
    st.write(response)

    # Show conversation memory
    # with st.expander('Topic '):
    #     st.info(topic_memory.buffer)

    # with st.expander('Example '):
    #     st.info(example_memory.buffer)
