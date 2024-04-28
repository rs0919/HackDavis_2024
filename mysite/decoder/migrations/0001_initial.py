# Generated by Django 4.2.11 on 2024-04-28 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ImgToDecode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='SecretMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('secret_msg', models.CharField(max_length=100)),
                ('secret_img', models.ImageField(upload_to='image_to_decode/')),
            ],
        ),
    ]