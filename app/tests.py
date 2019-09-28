from django.urls import reverse
from django.core.files.base import ContentFile
from django.core.files.uploadedfile import InMemoryUploadedFile, SimpleUploadedFile
from io import BytesIO
from rest_framework.test import APITestCase, APIClient, APIRequestFactory
from rest_framework.views import status
from app.views import ListCreateLetterView, ListCreateWordView
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


class BaseLetterViewTest(BaseViewTest):
    def setUp(self):
        # add test data
        self.random_letter = self.create_letter(self, self.create_name(), self.create_image())
        self.create_letter(self, self.create_name(), self.create_image())
        self.create_letter(self, self.create_name(), self.create_image())
        self.create_letter(self, self.create_name(), self.create_image())
        self.create_letter(self, self.create_name(), self.create_image())
        self.create_letter(self, self.create_name(), self.create_image())
        self.create_letter(self, self.create_name(), self.create_image())


class BaseWordViewTest(BaseViewTest):
    def setUp(self):
        self.random_word = self.create_word(self, self.create_name(), self.create_image())
        self.create_word(self, self.create_name(), self.create_image())
        self.create_word(self, self.create_name(), self.create_image())
        self.create_word(self, self.create_name(), self.create_image())
        self.create_word(self, self.create_name(), self.create_image())
        self.create_word(self, self.create_name(), self.create_image())
        self.create_word(self, self.create_name(), self.create_image())


class BasePostViewTest(APITestCase):
    @staticmethod
    def create_file_image(size=(100, 100), image_mode='RGB', image_format='PNG'):
        data = BytesIO()
        Image.new(image_mode, size).save(data, image_format)
        data.seek(0)
        return data

    def setUp(self):
        self.factory = APIRequestFactory()
        image = self.create_file_image(image_format='GIF')
        image_file = SimpleUploadedFile('front.png', image.getvalue())
        self.form_data = {'name': BaseViewTest.create_name(), 'image': image_file}


class GetAllLettersTest(BaseLetterViewTest):
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


class GetAllWordsTest(BaseWordViewTest):
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


class GetSingleLetterTest(BaseLetterViewTest):
    def setUp(self):
        super().setUp()

    def test_get_single_letters(self):
        """
        This test ensures that one of letter's gif added in the setUp method
        exist when we make a GET request to the letter/name endpoint
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


class GetSingleWordTest(BaseWordViewTest):
    def setUp(self):
        super().setUp()

    def test_get_single_words(self):
        """
        This test ensures that one of word's gif added in the setUp method
        exist when we make a GET request to the word/name endpoint
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


class DestroySingleLetterTest(BaseLetterViewTest):
    def setUp(self):
        super().setUp()

    def test_destroy_single_letters(self):
        """
        This test ensures that one of letter's gif added in the setUp method
        can be delete to the letter/name endpoint
        """
        # hit the API endpoint
        response = self.client.delete(
            reverse("letter-single", kwargs={'version': 'v1',
                                             'name': self.random_letter.name})
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class DestroySingleWordTest(BaseWordViewTest):
    def setUp(self):
        super().setUp()

    def test_destroy_single_words(self):    
        """
        This test ensures that one of word's gif added in the setUp method
        can be delete to the word/name endpoint
        """
        # hit the API endpoint
        response = self.client.delete(
            reverse("word-single", kwargs={'version': 'v1',
                                           'name': self.random_word.name})
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class PostNewLetterTest(BasePostViewTest):
    def test_post_single_letters(self):
        request = self.factory.post(
            reverse("letter-all", kwargs={'version': 'v1'}),
            self.form_data, format='multipart'
        )
        response = ListCreateLetterView.as_view()(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class PostNewWordTest(BasePostViewTest):
    def test_post_single_words(self):
        request = self.factory.post(
            reverse("word-all", kwargs={'version': 'v1'}),
            self.form_data, format='multipart'
        )
        response = ListCreateWordView.as_view()(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class UpdateSingleWordTest(BaseWordViewTest):
    def setUp(self):
        super().setUp()

    def test_update_single_word(self):
        """
        This test ensures that one of word's gif added in the setUp method
        can be updated to the word/name endpoint
        """
        # hit the API endpoint
        image = BasePostViewTest.create_file_image(image_format='GIF')
        image_file = SimpleUploadedFile('fotinha.png', image.getvalue())
        data = {'name': 'djikstra', 'image': image_file}
        response = self.client.put(
            reverse("word-single", kwargs={'version': 'v1',
                                           'name': self.random_word.name}),
            data, format='multipart'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        expected = Word.objects.filter(name='djikstra')
        serial = WordSerializer(expected, many=True)
        self.assertEqual(serial.data[0]['name'], data['name'])


class UpdateSingleLetterTest(BaseLetterViewTest):
    def setUp(self):
        super().setUp()

    def test_update_single_letter(self):
        """
        This test ensures that one of letters's gif added in the setUp method
        can be updated to the letter/name endpoint
        """
        # hit the API endpoint
        image = BasePostViewTest.create_file_image(image_format='GIF')
        image_file = SimpleUploadedFile('fotinha.png', image.getvalue())
        data = {'name': 'frobenius', 'image': image_file}
        response = self.client.put(
            reverse("letter-single", kwargs={'version': 'v1',
                                             'name': self.random_letter.name}),
            data, format='multipart'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        expected = Letter.objects.filter(name='frobenius')
        serial = LetterSerializer(expected, many=True)
        self.assertEqual(serial.data[0]['name'], data['name'])
