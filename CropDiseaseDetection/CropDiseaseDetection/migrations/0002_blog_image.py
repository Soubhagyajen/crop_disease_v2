# Generated by Django 5.1.7 on 2025-03-24 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CropDiseaseDetection', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='blog_images/'),
        ),
    ]
