# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-03 21:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('singup', '0008_auto_20170403_2023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='selfi',
            field=models.ImageField(upload_to='static/upload/'),
        ),
    ]