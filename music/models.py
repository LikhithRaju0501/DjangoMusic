from django.db import models


class Song(models.Model):
    name = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    song = models.FileField(upload_to='songd')
    image = models.ImageField(upload_to = 'pics')
