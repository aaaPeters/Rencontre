# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-01 08:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0009_auto_20170630_0518'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserPersonalInfo',
            fields=[
                ('userID', models.CharField(max_length=11, primary_key=True, serialize=False)),
                ('nickname', models.CharField(max_length=24)),
                ('profile', models.CharField(max_length=80)),
                ('birthday', models.DateField(blank=True, null=True)),
                ('address', models.CharField(blank=True, max_length=80, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('constellation', models.CharField(blank=True, max_length=6, null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('isVerificate', models.BooleanField(default=False)),
            ],
        ),
        migrations.RenameField(
            model_name='user',
            old_name='msg',
            new_name='Token',
        ),
        migrations.RemoveField(
            model_name='token',
            name='id',
        ),
        migrations.AddField(
            model_name='token',
            name='userID',
            field=models.CharField(default=1, max_length=11, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='personalInfo',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='User.UserPersonalInfo'),
            preserve_default=False,
        ),
    ]
