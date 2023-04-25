from django.urls import path
from .views import index,send_message,upload_pdf

urlpatterns = [
    path("",index,name="index"),
    path("send_message",send_message,name="send_message"),
    path("upload_pdf",upload_pdf,name="upload_pdf"),
]