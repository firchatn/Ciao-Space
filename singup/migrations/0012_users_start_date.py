# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-22 13:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('singup', '0011_auto_20170411_1545'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='start_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='date cheek'),
            preserve_default=False,
        ),
    ]