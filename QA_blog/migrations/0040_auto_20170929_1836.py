# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-29 18:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('QA_blog', '0039_auto_20170923_1537'),
    ]

    operations = [
        migrations.RenameField(
            model_name='video',
            old_name='guide_description',
            new_name='game_description',
        ),
        migrations.RenameField(
            model_name='video',
            old_name='guide_image',
            new_name='game_image',
        ),
        migrations.RenameField(
            model_name='video',
            old_name='guide_name',
            new_name='game_name',
        ),
        migrations.RenameField(
            model_name='video',
            old_name='guide_price',
            new_name='game_price',
        ),
    ]
