# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-22 18:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yhbot', '0008_auto_20170923_0148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school_info',
            name='published_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
