# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-02 20:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('singup', '0004_auto_20170402_2049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='selfi',
            field=models.ImageField(blank=True, upload_to='/upload/'),
        ),
    ]