# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-22 16:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yhbot', '0007_auto_20170918_0013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school_info',
            name='published_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
