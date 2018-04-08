# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-26 12:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ask_app', '0002_auto_20180107_0702'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='belong',
            new_name='answer',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='author',
            new_name='asker',
        ),
        migrations.RenameField(
            model_name='topic',
            old_name='Describe',
            new_name='content',
        ),
        migrations.RenameField(
            model_name='topic',
            old_name='text',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='agree',
        ),
        migrations.RemoveField(
            model_name='question',
            name='visitor',
        ),
        migrations.AddField(
            model_name='answer',
            name='down_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='answer',
            name='up_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='question',
            name='visi_count',
            field=models.IntegerField(default=0),
        ),
    ]