# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-29 21:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0008_auto_20170630_0506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='registerTime',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
