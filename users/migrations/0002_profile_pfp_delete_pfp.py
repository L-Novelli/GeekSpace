# Generated by Django 4.1.2 on 2023-01-16 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='pfp',
            field=models.ImageField(default='defautl.jpg', upload_to='profile_images'),
        ),
        migrations.DeleteModel(
            name='Pfp',
        ),
    ]