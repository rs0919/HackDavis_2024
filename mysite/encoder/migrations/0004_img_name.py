# Generated by Django 4.2.11 on 2024-04-28 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('encoder', '0003_remove_img_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='img',
            name='name',
            field=models.CharField(default='plain_image', max_length=50),
        ),
    ]
