# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-29 20:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0005_auto_20170630_0337'),
    ]

    operations = [
        migrations.AddField(
            model_name='token',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='token',
            name='token',
            field=models.CharField(max_length=32),
        ),
    ]
