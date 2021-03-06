# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-25 20:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('heartuser', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_message',
            field=models.TextField(default='i am guy looking for a girl'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profile',
            name='ethnicity',
            field=models.CharField(choices=[('1', 'White'), ('2', 'Black'), ('3', 'Asian')], max_length=30),
        ),
        migrations.AlterField(
            model_name='profile',
            name='religion',
            field=models.CharField(choices=[('1', 'Christianity'), ('2', 'Islam'), ('3', 'Judaism')], max_length=30),
        ),
    ]
