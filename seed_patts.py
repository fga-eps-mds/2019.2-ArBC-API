import os
import django
import string
import app
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.files.base import ContentFile

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api.settings')
django.setup()


def load_patts(patt_name):

    file_name = 'pattern-' + patt_name
    content_file = ContentFile(open('seeds_patts/' +
                                    file_name + '.patt', 'rb').read())
    return InMemoryUploadedFile(content_file, None,
                                file_name + '.patt', 'pattern',
                                content_file.tell, None)


def create_patt(number, letter):
    pattern = app.models.Pattern()
    pattern.name = letter + number
    patts = load_patts(pattern.name)
    pattern.patts.save(patts.name, patts)
    pattern.save()


for number in [1, 2]:
    for letter in string.ascii_uppercase:
        create_patt(number, letter)
