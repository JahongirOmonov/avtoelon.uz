# Generated by Django 3.2 on 2024-02-09 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avto', '0002_post_json'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='main_photo',
            field=models.ImageField(blank=True, editable=False, null=True, upload_to=''),
        ),
    ]
