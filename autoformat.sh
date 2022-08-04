#! /bin/sh
autoflake --remove-all-unused-imports --remove-unused-variables --remove-duplicate-keys \
  --recursive --in-place oc_lettings_site

isort oc_lettings_site

flake8 --ignore E203,E501,W503 oc_lettings_site

black --line-length=100 --exclude oc_lettings_site/lettings/api/migrations \
  --exclude oc_lettings_site/profiles/api/migrations \
  oc_lettings_site \
  $@

