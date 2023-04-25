from django.shortcuts import render
from .models import PdfFile
from django.contrib import messages

# Create your views here.

def index(request):        
    
    return render(request,"index.html")

def send_message(request):
    if request.method == "POST":
        message = request.POST.get("message")
        return render(request,"index.html",{"message":message}) 
    
def upload_pdf(request):
    if request.method == "POST":
        print("Reached Upload PDF")
        pdf_files = request.FILES.getlist("pdf_files")
        for pdf in pdf_files:
            PdfFile.objects.create(file=pdf)
        messages.success(request,"PDF Files are uploaded")
        return render(request,"index.html",{"pdf_files":pdf_files})