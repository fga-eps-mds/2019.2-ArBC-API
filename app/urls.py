from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import ListCreateWordView
from .views import ListCreateLetterView
from .views import RetrieveUpdateDestroyLetterView
from .views import RetrieveUpdateDestroyWordView


urlpatterns = [
    path('Word/', ListCreateWordView.as_view(), name="word-all"),
    path('Letter/', ListCreateLetterView.as_view(), name="letter-all"),
    path('Word/<name>', RetrieveUpdateDestroyWordView.as_view(), name="word-single"),
    path('Letter/<name>', RetrieveUpdateDestroyLetterView.as_view(), name="letter-single"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
