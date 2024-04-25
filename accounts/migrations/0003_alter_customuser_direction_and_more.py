# Generated by Django 5.0.2 on 2024-04-24 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_customuser_options_alter_customuser_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='direction',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name="Yo'nalish"),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='first_name',
            field=models.CharField(max_length=100, verbose_name='Ism'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='group',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Guruh'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='users/image', verbose_name='Rasm'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='last_name',
            field=models.CharField(max_length=100, verbose_name='Familiya'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='patronymic',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Otasining ismi'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='phone',
            field=models.CharField(blank=True, max_length=13, null=True, verbose_name='Telefon'),
        ),
    ]
