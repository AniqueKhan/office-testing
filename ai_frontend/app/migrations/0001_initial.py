# Generated by Django 4.2 on 2023-04-25 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PdfFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='pdf_files')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
