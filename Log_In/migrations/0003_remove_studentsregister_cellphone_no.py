# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-31 01:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Log_In', '0002_once'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentsregister',
            name='CellPhone_No',
        ),
    ]
