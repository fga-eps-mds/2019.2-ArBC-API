from __future__ import unicode_literals
from djongo import models

# Create your models here


class Gifs(models.Model):
    # gif title
    title = models.CharField(max_length=255, null=False)
    image = models.ImageField(upload_to='app/assets/')

    def str(self):
        return "{}".format(self.title)