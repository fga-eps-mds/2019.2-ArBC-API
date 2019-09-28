from rest_framework import serializers
from .models import Word
from .models import Letter


class WordSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(
        max_length=None, use_url=True
    )

    class Meta:
        model = Word
        fields = ("name", "image")


class LetterSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(
        max_length=None, use_url=True
    )

    class Meta:
        model = Letter
        fields = ("name", "image")
