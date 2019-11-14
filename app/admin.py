from django.contrib import admin
from .models import Word
from .models import Letter
from .models import Pattern
# Register your models here.

admin.site.register(Word)
admin.site.register(Letter)
admin.site.register(Pattern)
