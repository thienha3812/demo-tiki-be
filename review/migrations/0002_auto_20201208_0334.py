# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-12-08 03:34
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='time_created',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 8, 3, 34, 0, 997406, tzinfo=utc)),
        ),
    ]
