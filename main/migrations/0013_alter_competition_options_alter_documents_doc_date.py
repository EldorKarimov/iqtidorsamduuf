# Generated by Django 5.0.2 on 2024-04-23 05:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_competition_slug_alter_documents_doc_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='competition',
            options={'verbose_name': 'Tanlov', 'verbose_name_plural': 'Tanlovlar'},
        ),
        migrations.AlterField(
            model_name='documents',
            name='doc_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 23, 5, 9, 36, 573238, tzinfo=datetime.timezone.utc)),
        ),
    ]
