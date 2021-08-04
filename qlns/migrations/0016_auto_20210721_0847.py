# Generated by Django 3.2.3 on 2021-07-21 01:47

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qlns', '0015_auto_20210720_2239'),
    ]

    operations = [
        migrations.RenameField(
            model_name='giaichi',
            old_name='noidunggiaichi',
            new_name='giaichihanghoa',
        ),
        migrations.RemoveField(
            model_name='giaichi',
            name='hanghoagiaichi',
        ),
        migrations.AddField(
            model_name='giaichi',
            name='giaichikhac',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='giaichi',
            name='giaichithietbi',
            field=models.JSONField(blank=True, null=True, verbose_name='Trang Thiết Bị'),
        ),
    ]