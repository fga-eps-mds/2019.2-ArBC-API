from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import Word
from .models import Letter
from .serializers import WordSerializer
from .serializers import LetterSerializer
from PIL import Image
import tempfile
import random
import string


class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_image():
        image = Image.new('RGBA', size=(50, 50), color=(155, 0, 0))
        file = tempfile.NamedTemporaryFile(suffix='.png')
        image.save(file)
        return image

    @staticmethod
    def create_name(stringLength=10):
        name = string.ascii_lowercase
        return ''.join(random.choice(name) for i in range(stringLength))

    @staticmethod
    def create_word(self, title="", image=None):
        if title != "" and image is not None:
            Word.objects.create(title=title, image=None)

    @staticmethod
    def create_letter(self, title="", image=None):
        if title != "" and image is not None:
            Letter.objects.create(title=title, image=None)

    def setUp(self):
        # add test data
        self.create_letter(self.create_name(), self.create_image())
        self.create_letter(self.create_name(), self.create_image())
        self.create_letter(self.create_name(), self.create_image())
        self.create_letter(self.create_name(), self.create_image())
        self.create_letter(self.create_name(), self.create_image())
        self.create_letter(self.create_name(), self.create_image())
        
        self.create_word(self.create_name(), self.create_image())
        self.create_word(self.create_name(), self.create_image())
        self.create_word(self.create_name(), self.create_image())
        self.create_word(self.create_name(), self.create_image())
        self.create_word(self.create_name(), self.create_image())
        self.create_word(self.create_name(), self.create_image())

class GetAllLettersTest(BaseViewTest):
    def test_get_all_letters(self):
        """
        This test ensures that all letter's gifs added in the setUp method
        exist when we make a GET request to the letter/ endpoint
        """
        # hit the API endpoint
        response = self.client.get(
            reverse("letter-all", kwargs={"version": "v1"})
        )
        # fetch the data from db
        expected = Letter.objects.all()
        serialized = LetterSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetAllWordsTest(BaseViewTest):
    def test_get_all_words(self):
        """
        This test ensures that all word's gifs added in the setUp method
        exist when we make a GET request to the words endpoint
        """
        # hit the API endpoint
        response = self.client.get(
            reverse("word-all", kwargs={"version": "v1"})
        )
        # fetch the data from db
        expected = Word.objects.all()
        serialized = WordSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

