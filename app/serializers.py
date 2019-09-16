from rest_framework import serializers
from .models import Word
from .models import Letter


class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word
        fields = ("name", "image")


class LetterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Letter
        fields = ("name", "image")
