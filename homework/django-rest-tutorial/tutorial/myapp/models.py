from django.db import models


class Music(models.Model):
    title = models.CharField(max_length=30)
    genre = models.CharField(max_length=15)
    singer = models.CharField(max_length=30)