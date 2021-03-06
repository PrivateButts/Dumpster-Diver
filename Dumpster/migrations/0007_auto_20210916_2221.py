# Generated by Django 3.2.7 on 2021-09-17 02:21

import Dumpster.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dumpster', '0006_auto_20210916_1949'),
    ]

    operations = [
        migrations.AddField(
            model_name='audioasset',
            name='thumbnail',
            field=models.ImageField(blank=True, upload_to=Dumpster.models.get_thumb_upload_directory),
        ),
        migrations.AddField(
            model_name='modelasset',
            name='thumbnail',
            field=models.ImageField(blank=True, upload_to=Dumpster.models.get_thumb_upload_directory),
        ),
        migrations.AddField(
            model_name='textasset',
            name='thumbnail',
            field=models.ImageField(blank=True, upload_to=Dumpster.models.get_thumb_upload_directory),
        ),
        migrations.AddField(
            model_name='textureasset',
            name='thumbnail',
            field=models.ImageField(blank=True, upload_to=Dumpster.models.get_thumb_upload_directory),
        ),
        migrations.AddField(
            model_name='videoasset',
            name='thumbnail',
            field=models.ImageField(blank=True, upload_to=Dumpster.models.get_thumb_upload_directory),
        ),
    ]
