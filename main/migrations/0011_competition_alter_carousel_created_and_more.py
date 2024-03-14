# Generated by Django 5.0.2 on 2024-03-11 07:31

import ckeditor_uploader.fields
import datetime
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_documents_doc_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Competition',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='yaratilgan sana')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='yangilangan sana')),
                ('title', models.CharField(max_length=255, verbose_name='Sarlavha')),
                ('image', models.ImageField(upload_to='competition/images', verbose_name='Rasm')),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Matn')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='carousel',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='yaratilgan sana'),
        ),
        migrations.AlterField(
            model_name='carousel',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='yangilangan sana'),
        ),
        migrations.AlterField(
            model_name='documents',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='yaratilgan sana'),
        ),
        migrations.AlterField(
            model_name='documents',
            name='doc_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 11, 7, 31, 19, 16282, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='documents',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='yangilangan sana'),
        ),
        migrations.AlterField(
            model_name='startupprojects',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='yaratilgan sana'),
        ),
        migrations.AlterField(
            model_name='startupprojects',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='yangilangan sana'),
        ),
        migrations.AlterField(
            model_name='talentedstudents',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='yaratilgan sana'),
        ),
        migrations.AlterField(
            model_name='talentedstudents',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='yangilangan sana'),
        ),
    ]