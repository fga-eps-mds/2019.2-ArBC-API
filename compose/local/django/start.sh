#!/bin/sh

set -o errexit
set -o pipefail
set -o nounset
set -o xtrace


docker build -t registry.gitlab.com/lucianosz7/2019-2-arbc-api .
docker push registry.gitlab.com/lucianosz7/2019-2-arbc-api

python manage.py migrate
python manage.py runserver 0.0.0.0:8000
