from rest_framework import generics
from django.views.generic import FormView
from .forms import S3DirectUploadForm
from .models import Word
from .models import Letter
from .serializers import WordSerializer
from .serializers import LetterSerializer


class MyView(FormView):
    template_name = 'form.html'
    form_class = S3DirectUploadForm

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
