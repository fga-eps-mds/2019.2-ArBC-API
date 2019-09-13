from django.urls import path
from .views import ListGifsView


urlpatterns = [
    path('Gifs/', ListGifsView.as_view(), name="gifs-all")
]