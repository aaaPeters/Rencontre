# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-29 19:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0003_auto_20170629_0817'),
    ]

    operations = [
        migrations.CreateModel(
            name='Token',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=32)),
                ('deadLine', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='deadLine',
        ),
        migrations.AddField(
            model_name='user',
            name='salt',
            field=models.CharField(blank=True, max_length=32),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=32),
        ),
        migrations.AddField(
            model_name='user',
            name='msg',
            field=models.OneToOneField(default=22, on_delete=django.db.models.deletion.CASCADE, to='User.Token'),
            preserve_default=False,
        ),
    ]