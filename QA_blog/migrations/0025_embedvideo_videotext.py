# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-28 15:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QA_blog', '0024_embedvideo'),
    ]

    operations = [
        migrations.AddField(
            model_name='embedvideo',
            name='videotext',
            field=models.TextField(default=0),
        ),
    ]
