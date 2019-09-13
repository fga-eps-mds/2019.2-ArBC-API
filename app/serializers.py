from rest_framework import serializers
from .models import Gifs


class GifsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gifs
        fields = ("nome", "caminho")
