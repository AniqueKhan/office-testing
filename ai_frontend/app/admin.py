from django.contrib import admin
from .models import PdfFile,Message,Conversation
# Register your models here.

class PdfFileAdmin(admin.ModelAdmin):
    list_display = ("file","created_at")

admin.site.register(PdfFile,PdfFileAdmin)
admin.site.register((Message,Conversation))