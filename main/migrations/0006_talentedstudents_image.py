# Generated by Django 5.0.2 on 2024-02-28 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_talentedstudents_talent_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='talentedstudents',
            name='image',
            field=models.ImageField(default='assets/img/user.jpg', upload_to='talent-tudent/images'),
        ),
    ]
