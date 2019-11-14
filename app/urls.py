from django.urls import path
from .views import ListCreateWordView
from .views import ListCreateLetterView
from .views import ListPatternView
from .views import RetrieveUpdateDestroyLetterView
from .views import RetrieveUpdateDestroyWordView


urlpatterns = [
    path('Word/', ListCreateWordView.as_view(), name="word-all"),
    path('Letter/', ListCreateLetterView.as_view(), name="letter-all"),
    path('Pattern/', ListPatternView.as_view(), name="pattern-all"),
    path('Word/<name>', RetrieveUpdateDestroyWordView.as_view(),
         name="word-single"),
    path('Letter/<name>', RetrieveUpdateDestroyLetterView.as_view(),
         name="letter-single"),
]
