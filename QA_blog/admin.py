# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import Post
from QA_blog import models

admin.site.register(Post)
admin.site.register(models.Article)
admin.site.register(models.Reporter)
admin.site.register(models.Video)

