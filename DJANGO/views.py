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
from django.http import HttpResponse

load_dotenv()

apikey = os.getenv('GROQ_API_KEY')
llm = ChatGroq(temperature=0.6,model='llama-3.1-8b-instant',api_key=apikey)
vector_search = None






# Create your views here.
def home(request):
    return render(request, 'home.html')

def upload(request):
    message = None

    if request.method =="POST":
        form = PDFUploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['pdf_file']
            documents = []
        # file = request.FILES.get("document")
        # if file:
            #process_document(file)  #my RAG ingestion pipeline

    #         try:
    #             # Load and process the PDF
    #             pdf_reader = PdfReader(uploaded_file)
    #             for page in pdf_reader.pages:
    #                 text = page.extract_text()
    #                 if text:
    #                     doc = Document(page_content=text)
                        
    #        message = "Document Uploaded and Indexed!"
    # return render(request, 'upload.html',
    #               {'message':message})

def ask_questions(request):
    answer = None

    if request.method == "POST":
        question = request.POST.get("question")
        if question:
            answer = ask_questions(question) # my RAG query pipeline
    return render(request, 'ask_questions.html')