# Generated by Django 3.2.7 on 2021-09-14 06:48

import Dumpster.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Dumpster', '0002_auto_20210914_0156'),
    ]

    operations = [
        migrations.CreateModel(
            name='TextureAsset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('number', models.PositiveIntegerField()),
                ('file', models.FileField(upload_to=Dumpster.models.get_asset_upload_directory)),
                ('notes', models.TextField(blank=True)),
                ('asset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Dumpster.asset')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TextAsset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('number', models.PositiveIntegerField()),
                ('file', models.FileField(upload_to=Dumpster.models.get_asset_upload_directory)),
                ('notes', models.TextField(blank=True)),
                ('asset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Dumpster.asset')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ModelAsset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('number', models.PositiveIntegerField()),
                ('file', models.FileField(upload_to=Dumpster.models.get_asset_upload_directory)),
                ('notes', models.TextField(blank=True)),
                ('asset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Dumpster.asset')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]