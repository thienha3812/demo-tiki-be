# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-12-09 07:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0002_auto_20201208_0334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='time_created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
