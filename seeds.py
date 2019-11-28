import os
import django
import string
import app
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.files.base import ContentFile

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api.settings')
django.setup()


def load_image(name, folder):

    content_file = ContentFile(open(folder +
                                    name + '.gif', 'rb').read())
    return InMemoryUploadedFile(content_file, None,
                                name + '.gif', 'image/gif',
                                content_file.tell, None)


""" def create_letter(N):

    letter = app.models.Letter()
    letter.name = N
    image = load_image(N, 'seeds_letters/')
    letter.image.save(image.name, image)
    letter.save() """


def create_word(name):

    word = app.models.Word()
    word.name = name
    image = load_image(name, 'seeds_words/')
    word.image.save(image.name, image)
    word.save()


""" for i in string.ascii_uppercase:
    create_letter(i)


print('Letters have been successfully added') """


for file_name in os.listdir('./seeds_words'):
    if os.path.isfile('./seeds_words/' + file_name):
        word = file_name.replace('.gif', '')
        create_word(word)

print('Words have been successfully added')
