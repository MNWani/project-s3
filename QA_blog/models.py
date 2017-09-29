# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import uuid
from decimal import Decimal
from django.db import models
from django.utils import timezone
from django.conf import settings
from paypal.standard.forms import PayPalPaymentsForm


class Post(models.Model):
    """
    Here we'll define our Post model
    """

    # author is linked to a registered
    # user, via the User model in the auth app.
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    writer = models.CharField(max_length=70, blank=True, null=True)
    views = models.IntegerField(default=0)  # Record how often a post is seen
    tag = models.CharField(max_length=30, blank=True, null=True)  # Lets me see how often a post is seen
    post_image = models.ImageField(upload_to="images", blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __unicode__(self):
        return self.title


class Reporter(models.Model):
    full_name = models.CharField(max_length=70)

    def __unicode__(self):
        return self.full_name


RATINGS = (
    (1, 'Awful'),
    (2, 'Poor'),
    (3, 'Average'),
    (4, 'Good'),
    (5, 'Outstanding'),
)

class Article(models.Model):
    pub_date = models.DateField()
    headline = models.CharField(max_length=200)
    content = models.TextField()
    rating = models.IntegerField(choices=RATINGS)
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images", blank=True, null=True)

    def __unicode__(self):
        return self.headline
        
class Video(models.Model):
    title = models.CharField(max_length=70)
    description = models.CharField(max_length=200)
    link = models.URLField()
    game_name = models.CharField(max_length=254)
    game_image = models.ImageField(upload_to="images", blank=True, null=True)
    game_description = models.TextField(max_length=400, null=True, blank=True)
    game_price = models.DecimalField(max_digits=6, decimal_places=2, default=Decimal('0.00'))

    @property
    def paypal_form(self):
        paypal_dict = {
            "business": settings.PAYPAL_RECEIVER_EMAIL,
            "amount": self.game_price,
            "currency": "GBP",
            "item_name": self.game_name,
            "invoice": "%s-%s" % (self.pk, uuid.uuid4()),
            "notify_url": settings.PAYPAL_NOTIFY_URL,
            "return_url": "%s/paypal-return" % settings.SITE_URL,
            "cancel_return": "%s/paypal-cancel" % settings.SITE_URL
        }
 
        return PayPalPaymentsForm(initial=paypal_dict)
 
    def __unicode__(self):
        return self.title


    
