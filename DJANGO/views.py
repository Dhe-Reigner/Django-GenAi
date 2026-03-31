from django.shortcuts import render, redirect
from .forms import PDFUploadForm
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document
from langchain_community.embeddings.fastembed import FastEmbedEmbeddings
from langchain_community.vectorstores import Qdrant
from qdrant_client import QdrantClient
from langchain.chains import retrieval_qa
from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.getenv('GROQ_API_KEY')
llm = ChatGroq(temperature=0.6,model='llama-3.1-8b-instant',api_key=apikey)
vector_search = None






# Create your views here.
def home(requests):
    return render(requests, 'home.html')