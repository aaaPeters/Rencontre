# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-25 20:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('registerTime', models.DateTimeField(auto_created=True)),
                ('userID', models.CharField(max_length=11, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=18)),
            ],
        ),
    ]
