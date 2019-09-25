from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import ListWordView
from .views import ListLetterView
from .views import RetrieveLetterView
from .views import RetrieveWordView


urlpatterns = [
    path('Word/', ListWordView.as_view(), name="word-all"),
    path('Letter/', ListLetterView.as_view(), name="letter-all"),
    path('Word/<name>', RetrieveWordView.as_view(), name="word-single"),
    path('Letter/<name>', RetrieveLetterView.as_view(), name="letter-single")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
