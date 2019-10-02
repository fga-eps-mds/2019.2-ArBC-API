import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','api.settings')

import django
django.setup()

from app.models import Letter
from django.core.files.uploadedfile import InMemoryUploadedFile, \
    SimpleUploadedFile
from django.core.files.base import ContentFile
import string


def load_image(char):
    content_file = ContentFile(open('seeds/' + char + '.gif','rb').read())
    file_name = char
    image_file = InMemoryUploadedFile(content_file, None,
                                        file_name + '.gif',
                                        'image/gif', content_file.tell, None)

    return image_file

def creat_Letter(N):
    letter = Letter()
    letter.name = N
    image = load_image(N)
    letter.image.save(image.name, image)
    letter.save()

for i in string.ascii_uppercase:
    creat_Letter(i)
