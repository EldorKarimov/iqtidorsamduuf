# Generated by Django 5.0.2 on 2024-05-20 07:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_alter_documents_doc_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documents',
            name='doc_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 20, 7, 26, 27, 109163, tzinfo=datetime.timezone.utc)),
        ),
    ]
