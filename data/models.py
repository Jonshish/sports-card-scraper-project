from django.db import models
from datetime import datetime


class Data(models.Model):
    player = models.CharField(max_length=200, blank=True)
    sold_price = models.IntegerField(blank=True)
    bids = models.IntegerField(blank=True)
    sold_date = models.CharField(max_length=20, blank=True)
    card_link = models.URLField(max_length=500, blank=True)
    image_link = models.URLField(max_length=500, blank=True)

    def __str__(self):
        return self.player