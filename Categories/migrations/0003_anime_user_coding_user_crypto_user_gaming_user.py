# Generated by Django 4.1.2 on 2023-01-16 13:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Categories', '0002_rename_anime_anime_name_rename_coding_coding_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='anime',
            name='user',
            field=models.CharField(default=-1.0, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='coding',
            name='user',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='crypto',
            name='user',
            field=models.CharField(default=datetime.datetime(2023, 1, 16, 13, 24, 46, 85761, tzinfo=datetime.timezone.utc), max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gaming',
            name='user',
            field=models.CharField(default='Python', max_length=20),
            preserve_default=False,
        ),
    ]
