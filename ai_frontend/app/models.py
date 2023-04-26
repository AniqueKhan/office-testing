from django.db import models

# Create your models here.


class PdfFile(models.Model):
    file = models.FileField(upload_to="pdf_files")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.file}"

class Message(models.Model):
    human_message = models.CharField(max_length=255)
    ai_message = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.human_message}"

class Conversation(models.Model):
    messages = models.ManyToManyField(Message)
    created_at = models.DateTimeField(auto_now_add=True)
    selected_conversation = models.BooleanField(default=False)

    def __str__(self):
        if self.messages.exists():
            last_message = self.messages.last()
            return f"{last_message.human_message[:20]}..."
        return "Empty Conversation"
        