# !/usr/bin/env python
# encoding: utf-8

import os
import sys

REMOVE_PATHS = [
    '{% if not cookiecutter.contains_js_apps %} ckanext/{{ cookiecutter.short_name }}/theme/package.json {% endif %}'
]

for path in REMOVE_PATHS:
    path = path.strip()
    if path and os.path.exists(path):
        if os.path.isdir(path):
            os.rmdir(path)
        else:
            os.unlink(path)
