# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-09 12:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ask_app', '0006_auto_20180403_1345'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='is_anonymity',
            field=models.BooleanField(default=False),
        ),
    ]
