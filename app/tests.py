from django.urls import reverse
from django.core.files.base import ContentFile
from django.core.files.uploadedfile import InMemoryUploadedFile
from io import BytesIO
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import Word
from .models import Letter
from .serializers import WordSerializer
from .serializers import LetterSerializer
from PIL import Image
import random
import string


class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_name(stringLength=10):
        name = string.ascii_lowercase
        return ''.join(random.choice(name) for i in range(stringLength))

    @staticmethod
    def create_image():
        image = Image.new('RGBA', size=(50, 50), color=(random.randint(0, 255),
                                                        random.randint(0, 255),
                                                        random.randint(0, 255)))
        buffer_io = BytesIO()
        image.save(fp=buffer_io, format='GIF')
        content_file = ContentFile(buffer_io.getvalue())
        file_name = string.ascii_lowercase
        file_name = ''.join(random.choice(file_name) for i in range(10))
        image_file = InMemoryUploadedFile(content_file, None, file_name + '.gif',
                                          'image/gif', content_file.tell, None)
        return image_file

    @staticmethod
    def create_word(self, name="", image=None):
        if name != "" and image is not None:
            word = Word()
            word.name = name
            word.image.save(image.name, image)
            word.save()
            return word

    @staticmethod
    def create_letter(self, name="", image=None):
        if name != "" and image is not None:
            letter = Letter()
            letter.name = name
            letter.image.save(image.name, image)
            letter.save()
            return letter

    def setUp(self):
        # add test data
        self.random_letter = self.create_letter(self, self.create_name(), self.create_image())
        self.create_letter(self, self.create_name(), self.create_image())
        self.create_letter(self, self.create_name(), self.create_image())
        self.create_letter(self, self.create_name(), self.create_image())
        self.create_letter(self, self.create_name(), self.create_image())
        self.create_letter(self, self.create_name(), self.create_image())
        self.create_letter(self, self.create_name(), self.create_image())

        self.random_word = self.create_word(self, self.create_name(), self.create_image())
        self.create_word(self, self.create_name(), self.create_image())
        self.create_word(self, self.create_name(), self.create_image())
        self.create_word(self, self.create_name(), self.create_image())
        self.create_word(self, self.create_name(), self.create_image())
        self.create_word(self, self.create_name(), self.create_image())
        self.create_word(self, self.create_name(), self.create_image())


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
        response_status = response.status_code
        response = response.data
        expected = Letter.objects.all()
        serialized = LetterSerializer(expected, many=True)
        serialized = serialized.data
        for i in range(len(serialized)):
            resp = response[i]
            serial = serialized[i]
            self.assertEqual(resp['name'], serial['name'])
            path = resp['image']
            path = path[17:len(path)]  # removing the localhost and http prefix
            self.assertEqual(path, serial['image'])
        self.assertEqual(response_status, status.HTTP_200_OK)


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
        response_status = response.status_code
        response = response.data
        expected = Word.objects.all()
        serialized = WordSerializer(expected, many=True)
        serialized = serialized.data
        for i in range(len(serialized)):
            resp = response[i]
            serial = serialized[i]
            self.assertEqual(resp['name'], serial['name'])
            path = resp['image']
            path = path[17:len(path)]  # removing the localhost and http prefix
            self.assertEqual(path, serial['image'])
        self.assertEqual(response_status, status.HTTP_200_OK)


class GetSingleLetterTest(BaseViewTest):
    def setUp(self):
        super().setUp()

    def test_get_single_letters(self):
        """
        This test ensures that one of letter's gif added in the setUp method
        exist when we make a GET request to the letter/pk endpoint
        """
        # hit the API endpoint
        response = self.client.get(
            reverse("letter-single", kwargs={'version': 'v1',
                                             'name': self.random_letter.name})
        )
        # fetch the data from db
        response_status = response.status_code
        expected = Letter.objects.filter(name=self.random_letter.name)
        serialized = LetterSerializer(expected, many=True)
        serialized = serialized.data[0]
        response = response.data
        self.assertEqual(response['name'], serialized['name'])
        path = response['image']
        path = path[17:len(path)]  # removing the localhost and http prefix
        self.assertEqual(path, serialized['image'])
        self.assertEqual(response_status, status.HTTP_200_OK)


class GetSingleWordTest(BaseViewTest):
    def setUp(self):
        super().setUp()

    def test_get_single_words(self):
        """
        This test ensures that one of word's gif added in the setUp method
        exist when we make a GET request to the letter/pk endpoint
        """
        # hit the API endpoint
        response = self.client.get(
            reverse("word-single", kwargs={'version': 'v1',
                                           'name': self.random_word.name})
        )
        # fetch the data from db
        response_status = response.status_code
        expected = Word.objects.filter(name=self.random_word.name)
        serialized = WordSerializer(expected, many=True)
        serialized = serialized.data[0]
        response = response.data
        self.assertEqual(response['name'], serialized['name'])
        path = response['image']
        path = path[17:len(path)]  # removing the localhost and http prefix
        self.assertEqual(path, serialized['image'])
        self.assertEqual(response_status, status.HTTP_200_OK)
