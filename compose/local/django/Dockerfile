FROM python:3.6-alpine

ENV PYTHONUNBUFFERED 1

RUN apk update
  # psycopg2 dependencies
RUN apk add --virtual build-deps gcc python3-dev musl-dev 
RUN apk add postgresql-dev 
  # Pillow dependencies
RUN apk add jpeg-dev zlib-dev freetype-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev 
  # CFFI dependencies
RUN apk add libffi-dev py-cffi 
  # Translations dependencies
RUN apk add gettext 
  # https://docs.djangoproject.com/en/dev/ref/django-admin/#dbshell
RUN apk add postgresql-client 
RUN apk add --no-cache postgresql-libs 
# Requirements are installed here to ensure they will be cached.
COPY ./requirements /requirements
RUN pip install -r /requirements/local.txt

COPY ./compose/local/django/start.sh /start.sh
RUN sed -i 's/\r//' /start.sh
RUN chmod +x /start.sh

WORKDIR /app
