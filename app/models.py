from __future__ import unicode_literals
from djongo import models

# Create your models here.

class Gifs(models.Model):
    # gif title
    nome = models.CharField(max_length=255, null=False)
    # name of artist
    caminho = models.CharField(max_length=255, null=False)

    def __str__(self):
        return "{} - {}".format(self.nome, self.caminho)
