from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import Gifs
from .serializers import GifsSerializer


# Create your tests here.
# tests for views

class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_gifs(nome="", caminho=""):
        if nome != "" and caminho != "":
            Gifs.objects.create(nome=nome, caminho="")

    def setUp(self):
        #add test data
        self.create_gifs("#125ZH8966", "CJ")
        self.create_gifs("#771YXD898", "Baiano")
        self.create_gifs("#Y25HH8969", "Konca")
        self.create_gifs("#LLLPO8910", "Biruleibe")

class GetAllGifsTest(BaseViewTest):
    def test_get_all_gifs(self):
        """
        This test ensures that all gifs added in the setUp method
        exist when we make a GET request to the gifs/ endpoint
        """
        #hit the API endpoint
        response = self.client.get(
            reverse("gifs-all", kwargs={"version": "v1"})
        )
        # fetch the data from db
        expected = Gifs.objects.all()
        serialized = GifsSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
