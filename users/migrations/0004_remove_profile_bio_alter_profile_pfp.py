# Generated by Django 4.1.2 on 2023-01-19 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_remove_profile_avatar_alter_profile_pfp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='bio',
        ),
        migrations.AlterField(
            model_name='profile',
            name='pfp',
            field=models.ImageField(blank=True, null=True, upload_to='profile_images'),
        ),
    ]
