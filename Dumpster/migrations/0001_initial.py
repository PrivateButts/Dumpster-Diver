# Generated by Django 3.2.7 on 2021-09-14 05:49

import Dumpster.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=200)),
                ('source', models.CharField(blank=True, max_length=200)),
                ('author', models.CharField(blank=True, max_length=200)),
                ('attribution_required', models.BooleanField(default=False)),
                ('attribution_text', models.TextField(blank=True)),
                ('type', models.CharField(choices=[('image', 'Image'), ('audio', 'Audio'), ('video', 'Video'), ('text', 'Snippet'), ('texture', 'Texture'), ('model', 'Model')], max_length=10)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='VideoAsset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('number', models.PositiveIntegerField()),
                ('file', models.FileField(upload_to=Dumpster.models.get_asset_upload_directory)),
                ('notes', models.TextField()),
                ('asset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Dumpster.asset')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ImageAsset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('number', models.PositiveIntegerField()),
                ('file', models.FileField(upload_to=Dumpster.models.get_asset_upload_directory)),
                ('notes', models.TextField()),
                ('asset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Dumpster.asset')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AudioAsset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('number', models.PositiveIntegerField()),
                ('file', models.FileField(upload_to=Dumpster.models.get_asset_upload_directory)),
                ('notes', models.TextField()),
                ('asset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Dumpster.asset')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
