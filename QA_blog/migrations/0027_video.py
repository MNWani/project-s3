# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-09 10:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QA_blog', '0026_delete_embedvideo'),
    ]

    operations = [
        migrations.CreateModel(
            name='video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70)),
                ('description', models.CharField(max_length=200)),
                ('link', models.URLField()),
            ],
        ),
    ]
