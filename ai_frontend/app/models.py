from django.db import models

# Create your models here.


# class Message(models.Model):
#     body = models.TextField()

class PdfFile(models.Model):
    file = models.FileField(upload_to="pdf_files")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.file}"
