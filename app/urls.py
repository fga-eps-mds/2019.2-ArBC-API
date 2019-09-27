from django.urls import path
from .views import ListWordView
from .views import ListLetterView


urlpatterns = [
    path('Word/', ListWordView.as_view(), name="word-all"),
    path('Letter/', ListLetterView.as_view(), name="letter-all")
]