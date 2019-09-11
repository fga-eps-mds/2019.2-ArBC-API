from rest_framework import generics
from .models import Gifs
from .serializers import GifsSerializer


class ListGifsView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Gifs.objects.all()
    serializer_class = GifsSerializer