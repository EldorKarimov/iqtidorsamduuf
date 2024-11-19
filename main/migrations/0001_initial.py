# Generated by Django 5.0.2 on 2024-11-19 12:33

import ckeditor_uploader.fields
import datetime
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carousel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='yaratilgan sana')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='yangilangan sana')),
                ('image', models.ImageField(upload_to='carousel', verbose_name='Image')),
                ('content', models.CharField(blank=True, max_length=150, null=True, verbose_name='content 1')),
                ('content_uz', models.CharField(blank=True, max_length=150, null=True, verbose_name='content 1')),
                ('content_en', models.CharField(blank=True, max_length=150, null=True, verbose_name='content 1')),
                ('content_ru', models.CharField(blank=True, max_length=150, null=True, verbose_name='content 1')),
                ('content2', models.CharField(blank=True, max_length=255, null=True, verbose_name='content 2')),
                ('content2_uz', models.CharField(blank=True, max_length=255, null=True, verbose_name='content 2')),
                ('content2_en', models.CharField(blank=True, max_length=255, null=True, verbose_name='content 2')),
                ('content2_ru', models.CharField(blank=True, max_length=255, null=True, verbose_name='content 2')),
            ],
            options={
                'verbose_name': 'Carousel',
                'verbose_name_plural': 'Carousels',
            },
        ),
        migrations.CreateModel(
            name='Competition',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='yaratilgan sana')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='yangilangan sana')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('title_uz', models.CharField(max_length=255, null=True, verbose_name='title')),
                ('title_en', models.CharField(max_length=255, null=True, verbose_name='title')),
                ('title_ru', models.CharField(max_length=255, null=True, verbose_name='title')),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('image', models.ImageField(upload_to='competition/images', verbose_name='image')),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='desctiption')),
                ('description_uz', ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='desctiption')),
                ('description_en', ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='desctiption')),
                ('description_ru', ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='desctiption')),
            ],
            options={
                'verbose_name': 'Competition',
                'verbose_name_plural': 'Competitions',
            },
        ),
        migrations.CreateModel(
            name='Documents',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='yaratilgan sana')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='yangilangan sana')),
                ('doc_type', models.PositiveSmallIntegerField(choices=[(1, 'Buyruqlar'), (2, 'Nizomlar')], verbose_name='document type')),
                ('file_name', models.CharField(max_length=255, verbose_name='file name')),
                ('file_name_uz', models.CharField(max_length=255, null=True, verbose_name='file name')),
                ('file_name_en', models.CharField(max_length=255, null=True, verbose_name='file name')),
                ('file_name_ru', models.CharField(max_length=255, null=True, verbose_name='file name')),
                ('file', models.FileField(upload_to='uploads/doc/files', verbose_name='file')),
                ('doc_date', models.DateTimeField(default=datetime.datetime(2024, 11, 19, 12, 33, 11, 74703, tzinfo=datetime.timezone.utc))),
            ],
            options={
                'verbose_name_plural': 'Regulatory documents',
            },
        ),
        migrations.CreateModel(
            name='StartUpProjects',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='yaratilgan sana')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='yangilangan sana')),
                ('title', models.CharField(max_length=150, unique=True, verbose_name='title')),
                ('title_uz', models.CharField(max_length=150, null=True, unique=True, verbose_name='title')),
                ('title_en', models.CharField(max_length=150, null=True, unique=True, verbose_name='title')),
                ('title_ru', models.CharField(max_length=150, null=True, unique=True, verbose_name='title')),
                ('slug', models.SlugField(max_length=150, unique=True)),
                ('image', models.ImageField(upload_to='startup/images', verbose_name='image')),
                ('content', models.TextField(verbose_name="Loyiha ta'rifi")),
                ('content_uz', models.TextField(null=True, verbose_name="Loyiha ta'rifi")),
                ('content_en', models.TextField(null=True, verbose_name="Loyiha ta'rifi")),
                ('content_ru', models.TextField(null=True, verbose_name="Loyiha ta'rifi")),
                ('is_available', models.BooleanField(default=False, verbose_name='is available')),
            ],
            options={
                'verbose_name': 'startup project',
                'verbose_name_plural': 'startup projects',
            },
        ),
        migrations.CreateModel(
            name='TalentedStudents',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='yaratilgan sana')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='yangilangan sana')),
                ('first_name', models.CharField(max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(max_length=150, verbose_name='last name')),
                ('patronymic', models.CharField(max_length=150, verbose_name='patronymic')),
                ('image', models.ImageField(blank=True, null=True, upload_to='talent-tudent/images', verbose_name='student image')),
                ('teacher_full_name', models.CharField(max_length=255, verbose_name='teacher full name')),
                ('description', models.TextField(blank=True, null=True, verbose_name='student description')),
                ('description_uz', models.TextField(blank=True, null=True, verbose_name='student description')),
                ('description_en', models.TextField(blank=True, null=True, verbose_name='student description')),
                ('description_ru', models.TextField(blank=True, null=True, verbose_name='student description')),
                ('is_available', models.BooleanField(default=False, verbose_name='is available')),
                ('talent_type', models.CharField(choices=[('PRESIDENT', 'presidential stipendium holers'), ('STATE', 'Davlat stipendiatlar'), ('TALENT', 'talent students')], default='TALENT', max_length=15, verbose_name='talent type')),
            ],
            options={
                'verbose_name': 'Talent student',
                'verbose_name_plural': 'talent students',
            },
        ),
    ]
