help:
  just --list

install:
  pip install -r requirements.txt

site dir:
  python generate_site.py {{dir}}
