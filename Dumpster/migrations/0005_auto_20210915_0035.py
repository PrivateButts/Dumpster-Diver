# Generated by Django 3.2.7 on 2021-09-15 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dumpster', '0004_textasset_syntax_highlighting_language'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='textasset',
            name='file',
        ),
        migrations.AddField(
            model_name='textasset',
            name='text',
            field=models.TextField(default='Empty'),
            preserve_default=False,
        ),
    ]
