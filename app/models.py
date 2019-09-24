from __future__ import unicode_literals
from djongo import models


# Create your models here


class Word(models.Model):
    # gif title
    name = models.CharField(max_length=255, null=False)
    image = models.ImageField(upload_to='/word/')

    def str(self):
        return "{}".format(self.name)


class Letter(models.Model):
    # gif title
    name = models.CharField(max_length=255, null=False)
    image = models.ImageField(upload_to='/letter/')

    def str(self):
        return "{}".format(self.name)
