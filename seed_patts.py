import os
import django
import string
import app
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.files.base import ContentFile

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api.settings')
django.setup()


def load_patts(char, number):

    file_name = 'pattern-' + char + number
    content_file = ContentFile(open('seeds_patts/' + file_name + '.patt', 'rb').read())
    return InMemoryUploadedFile(content_file, None,
                                      file_name + '.patt', 'pattern',
                                      content_file.tell, None)

def create_patt(N):
    patt = app.models.Letter()
    letter.name = N
    image = load_patts(N)
    letter.image.save(image.name, image)
    letter.save()


for i in string.ascii_uppercase:
    creat_Letter(i)
