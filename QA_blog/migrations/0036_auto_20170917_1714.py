# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-17 17:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QA_blog', '0035_auto_20170917_1714'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='name',
            field=models.CharField(max_length=254),
        ),
    ]
