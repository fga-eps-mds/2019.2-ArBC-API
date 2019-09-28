from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import Word
from .serializers import WordSerializer


# Create your tests here.
# tests for views

class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_word(title="", image=""):
        if title != "" and image != "":
            Word.objects.create(title=title, image="")

    def setUp(self):
        #add test data
        self.create_word("#125ZH8966", "CJ")
        self.create_word("#771YXD898", "Baiano")
        self.create_word("#Y25HH8969", "Konca")
        self.create_word("#LLLPO8910", "Biruleibe")

class GetAllGifsTest(BaseViewTest):
    def test_get_all_gifs(self):
        """
        This test ensures that all gifs added in the setUp method
        exist when we make a GET request to the gifs/ endpoint
        """
        #hit the API endpoint
        response = self.client.get(
            reverse("word-all", kwargs={"version": "v1"})
        )
        # fetch the data from db
        expected = Word.objects.all()
        serialized = WordSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)