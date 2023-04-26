from django.shortcuts import render,redirect
from .models import PdfFile,Conversation,Message
from django.contrib import messages

# Create your views here.

def index(request):        
    conversations = Conversation.objects.all().order_by('-created_at')
    selected_conversation = Conversation.objects.filter(selected_conversation=True).first()
    context = {
        "conversations":conversations,
        "selected_conversation":selected_conversation,
    }
    return render(request,"index.html",context)

def send_message(request):
    if request.method == "POST":
        message = request.POST.get("message")
        message_object = Message.objects.create(human_message=message,ai_message="Hard Coded Response")
        conversations = Conversation.objects.all().order_by('-created_at')
        selected_conversation = Conversation.objects.filter(selected_conversation=True).first()
        selected_conversation.messages.add(message_object)
        selected_conversation.save()
        context = {
            "conversations":conversations,
            "selected_conversation":selected_conversation,
        }
        return render(request,"index.html",context)
    
def upload_pdf(request):
    if request.method == "POST":
        print("Reached Upload PDF")
        pdf_files = request.FILES.getlist("pdf_files")
        for pdf in pdf_files:
            PdfFile.objects.create(file=pdf)
        messages.success(request,"PDF File(s) are uploaded")
        # return render(request,"index.html",{"pdf_files":pdf_files})
        return redirect("index")
    
def select_conversation(request,conversation_id):
    conversation = Conversation.objects.get(pk=conversation_id)
    if not conversation.selected_conversation: 
        conversation.selected_conversation = True
        conversation.save()
        already_selected_conversation = Conversation.objects.filter(selected_conversation=True).exclude(pk=conversation_id).first()
        if already_selected_conversation:
            already_selected_conversation.selected_conversation = False
            already_selected_conversation.save()
    return redirect("index")

def new_conversation(request):

    message = Message.objects.create(human_message="Conversation Initialized",ai_message="Thank You For Initializing A Conversation!")
    new_conversation = Conversation.objects.create(selected_conversation=True)
    new_conversation.messages.add(message)
    new_conversation.save()
    already_selected_conversation = Conversation.objects.filter(selected_conversation=True).exclude(pk=new_conversation.pk).first()
    if already_selected_conversation:
        already_selected_conversation.selected_conversation = False
        already_selected_conversation.save()
    return redirect("index")