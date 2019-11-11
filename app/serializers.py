from rest_framework import serializers
from .models import Word
from .models import Letter
from .models import Pattern


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


class PatternSerializer(serializers.ModelSerializer):
    pattern = serializers.FileField(
        max_length=None, use_url=True
    )

    class Meta:
        ordering = ['-id']
        model = Pattern
        fields = ("name", "pattern")
