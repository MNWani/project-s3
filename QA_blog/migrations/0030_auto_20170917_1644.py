# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-17 16:44
from __future__ import unicode_literals

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QA_blog', '0029_post_writer'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='guide_description',
            field=models.TextField(blank=True, max_length=400, null=True),
        ),
        migrations.AddField(
            model_name='video',
            name='guide_name',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='video',
            name='guide_price',
            field=models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=6),
        ),
    ]
