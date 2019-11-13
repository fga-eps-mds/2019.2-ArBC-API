from rest_framework import generics
from .models import Word
from .models import Letter
from .models import Pattern
from .serializers import WordSerializer
from .serializers import LetterSerializer
from .serializers import PatternSerializer


class ListCreateWordView(generics.ListCreateAPIView):
    """
    Provides a list method handler.
    """
    queryset = Word.objects.all().order_by('id')
    serializer_class = WordSerializer


class ListCreateLetterView(generics.ListCreateAPIView):
    """
    Provides a list create method handler.
    """
    queryset = Letter.objects.all().order_by('id')
    serializer_class = LetterSerializer


class ListPatternView(generics.ListAPIView):
    """
    Provides a list create method handler.
    """
    queryset = Pattern.objects.all().order_by('id')
    serializer_class = PatternSerializer


class RetrieveUpdateDestroyWordView(generics.RetrieveUpdateDestroyAPIView):
    """
    Provides a retrieve update destroy method handler.
    """
    queryset = Word.objects.all()
    serializer_class = WordSerializer
    lookup_field = 'name'


class RetrieveUpdateDestroyLetterView(generics.RetrieveUpdateDestroyAPIView):
    """
    Provides a retrieve update destroy method handler.
    """
    queryset = Letter.objects.all()
    serializer_class = LetterSerializer
    lookup_field = 'name'
