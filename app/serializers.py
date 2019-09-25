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

    def get_image_url(self, obj):
        request = self.context.get('request')
        image_url = obj.image.url
        if request:
            return request.build_absolute_uri(image_url)
        else:
            return image_url


class LetterSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField('get_image_url')

    class Meta:
        model = Letter
        fields = ("name", "image")

    def get_image_url(self, obj):
        request = self.context.get('request')
        image_url = obj.image.url
        if request:
            return request.build_absolute_uri(image_url)
        else:
            return image_url
