# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-14 12:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('art', '0006_auto_20180814_2020'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='art',
            name='content',
        ),
    ]
