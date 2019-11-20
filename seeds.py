import os
import django
import string
import app
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.files.base import ContentFile

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api.settings')
django.setup()


def load_image(char):

    file_name = char
    content_file = ContentFile(open('seeds_letters/' +
                                    file_name + '.gif', 'rb').read())
    return InMemoryUploadedFile(content_file, None,
                                file_name + '.gif', 'image/gif',
                                content_file.tell, None)


def create_letter(N):

    letter = app.models.Letter()
    letter.name = N
    image = load_image(N)
    letter.image.save(image.name, image)
    letter.save()


for i in string.ascii_uppercase:
    create_letter(i)


print('Letters have been successfully added')
