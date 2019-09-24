from rest_framework import serializers
from .models import Word
from .models import Letter


class WordSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField('get_image_url')

    class Meta:
        model = Word
        fields = ("name", "image")

    def get_image_url(self, obj):
        return obj.image.url


class LetterSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField('get_image_url')

    class Meta:
        model = Letter
        fields = ("name", "image")

    def get_image_url(self, obj):
        return obj.image.url
