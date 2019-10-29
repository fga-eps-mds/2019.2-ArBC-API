from rest_framework import serializers
from .models import Word
from .models import Letter


class WordSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(
        max_length=None, use_url=True
    )

    class Meta:
        ordering = ['-id']
        model = Word
        fields = ("name", "image")


class LetterSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(
        max_length=None, use_url=True
    )

    class Meta:
        ordering = ['-id']
        model = Letter
        fields = ("name", "image")
