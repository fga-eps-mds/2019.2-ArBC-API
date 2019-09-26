from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import ListWordView
from .views import ListLetterView
from .views import RetrieveDestroyLetterView
from .views import RetrieveDestroyWordView


urlpatterns = [
    path('Word/', ListWordView.as_view(), name="word-all"),
    path('Letter/', ListLetterView.as_view(), name="letter-all"),
    path('Word/<name>', RetrieveDestroyWordView.as_view(), name="word-single"),
    path('Letter/<name>', RetrieveDestroyLetterView.as_view(), name="letter-single"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
