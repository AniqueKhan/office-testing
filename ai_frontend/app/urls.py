from django.urls import path
from .views import index,send_message,upload_pdf,select_conversation,new_conversation

urlpatterns = [
    path("",index,name="index"),
    path("send_message",send_message,name="send_message"),
    path("upload_pdf",upload_pdf,name="upload_pdf"),
    path("select_conversation/<int:conversation_id>",select_conversation,name="select_conversation"),
    path("new_conversation",new_conversation,name="new_conversation"),
]