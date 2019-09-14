from django.db import models

# Create your models here.

class Gifs(models.Model):
    # gif title
    title = models.CharField(max_length=255, null=False)
    # name of artist
    artist = models.CharField(max_length=255, null=False)

    def __str__(self):
        return "{} - {}".format(self.title, self.artist)