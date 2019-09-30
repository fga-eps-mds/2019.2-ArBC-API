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


""" from django.contrib.auth.models import User, Group
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name'] """
