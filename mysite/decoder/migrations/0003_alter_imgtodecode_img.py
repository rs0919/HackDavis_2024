# Generated by Django 4.2.11 on 2024-04-28 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('decoder', '0002_alter_imgtodecode_img_alter_secretmessage_secret_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imgtodecode',
            name='img',
            field=models.ImageField(upload_to='images_to_decode/encoded_image.png'),
        ),
    ]
