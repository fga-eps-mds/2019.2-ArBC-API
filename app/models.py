from __future__ import unicode_literals
from djongo import models


# Create your models here


class Word(models.Model):
    # gif title
    name = models.CharField(max_length=255, null=False)
    image = models.ImageField(upload_to='app/assets/word/')

    def str(self):
        return "{}".format(self.name)


class Letter(models.Model):
    # gif title
    name = models.CharField(max_length=255, null=False)
    image = models.ImageField(upload_to='app/assets/letter/')

    def str(self):
        return "{}".format(self.name)
