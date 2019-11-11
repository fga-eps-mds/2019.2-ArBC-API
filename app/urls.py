from django.urls import path
from .views import ListCreateWordView
from .views import ListCreateLetterView
from .views import ListCreatePatternView
from .views import RetrieveUpdateDestroyLetterView
from .views import RetrieveUpdateDestroyWordView
from .views import RetrieveUpdateDestroyPatternView


urlpatterns = [
    path('Word/', ListCreateWordView.as_view(), name="word-all"),
    path('Letter/', ListCreateLetterView.as_view(), name="letter-all"),
    path('Pattern/', ListCreatePatternView.as_view(), name="pattern-all"),
    path('Word/<name>', RetrieveUpdateDestroyWordView.as_view(),
         name="word-single"),
    path('Letter/<name>', RetrieveUpdateDestroyLetterView.as_view(),
         name="letter-single"),
    path('Pattern/<name>', RetrieveUpdateDestroyPatternView.as_view(),
         name="pattern-single"),
]
