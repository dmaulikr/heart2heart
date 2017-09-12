# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-29 08:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('heartuser', '0002_auto_20170725_2037'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_photo',
            field=models.ImageField(default='', upload_to='profilephotos'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profile',
            name='pets',
            field=models.CharField(choices=[('1', 'Dog'), ('2', 'Cat'), ('3', 'Guinea Pig')], max_length=30),
        ),
    ]