from rest_framework import generics
from .models import Word
from .models import Letter
from .serializers import WordSerializer
from .serializers import LetterSerializer


class ListWordView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Word.objects.all()
    serializer_class = WordSerializer


class ListLetterView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Letter.objects.all()
    serializer_class = LetterSerializer


class RetrieveWordView(generics.RetrieveAPIView):
    """
    Provides a retrieve method handler
    """
    queryset = Word.objects.all()
    serializer_class = WordSerializer
    lookup_field = 'name'


class RetrieveLetterView(generics.RetrieveAPIView):
    """
    Provides a retrieve method handler
    """
    queryset = Letter.objects.all()
    serializer_class = LetterSerializer
    lookup_field = 'name'
