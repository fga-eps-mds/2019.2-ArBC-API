from __future__ import unicode_literals
from django.db import models
from django.dispatch import receiver
from s3direct.fields import S3DirectField


# Create your models here


class Word(models.Model):

    # gif title
    name = models.CharField(max_length=255, null=False)
    image = models.ImageField(upload_to='word/')
    image_s3 = S3DirectField(dest='primary_destination', blank=True)

    def str(self):
        return "{}".format(self.name)


class Letter(models.Model):
    # gif title
    name = models.CharField(max_length=255, null=False)
    image = models.ImageField(upload_to='letter/')
    image_s3 = S3DirectField(dest='primary_destination', blank=True)

    def str(self):
        return "{}".format(self.name)


@receiver(models.signals.post_delete, sender=Word)
@receiver(models.signals.post_delete, sender=Letter)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding Word object is deleted.
    """
    if instance.image:
        instance.image.delete(False)


@receiver(models.signals.pre_save, sender=Word)
def auto_delete_word_image_on_change(sender, instance, **kwargs):
    """
    Deletes old file from filesystem
    when corresponding Word object is updated
    with new file.
    """
    if not instance.pk:
        return False

    try:
        old_file = Word.objects.get(pk=instance.pk).image
    except Word.DoesNotExist:
        return False

    new_file = instance.image
    if not old_file == new_file:
        old_file.delete(False)


@receiver(models.signals.pre_save, sender=Letter)
def auto_delete_letter_image_on_change(sender, instance, **kwargs):
    """
    Deletes old file from filesystem
    when corresponding Word object is updated
    with new file.
    """
    if not instance.pk:
        return False

    try:
        old_file = Letter.objects.get(pk=instance.pk).image
    except Letter.DoesNotExist:
        return False

    new_file = instance.image
    if not old_file == new_file:
        old_file.delete(False)
