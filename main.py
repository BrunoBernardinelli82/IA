# pip install langchain
# pip install langchain-community
# pip install langchain-huggingface
# pip install streamlit
# pip install python-dotenv
# pip install torch==2.3.1 torchvision torchaudio
# pip install -q transformers einops accelerate bitsandbytes
# pip install langchain-ollama
# pip install langchain-openai

import streamlit as st
from langchain_core.messages import AIMessage, HumanMessage
from langchain_core.prompts import MessagesPlaceholder

from langchain_ollama import ChatOllama
from langchain_openai import ChatOpenAI

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

import torch
from langchain_huggingface import ChatHuggingFace
from langchain_community.llms import huggingface_hub

from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="Seu Assistente Virtual ", page_icon="")
st.title("Seu Assistente Virtual")
st.button("Botao")
st.chat_input("Digite sua mensagem")
