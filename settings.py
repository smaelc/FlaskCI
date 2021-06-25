# coding: utf-8

import os
from flask import Flask

BASE_DIR        = os.path.dirname(__name__)
TEMPLATES_DIR   = os.path.join(BASE_DIR, 'templates')
STATIC_DIR      = os.path.join(BASE_DIR, 'static')

app             = Flask(__name__,
                        static_url_path=STATIC_DIR,
                        template_folder=TEMPLATES_DIR
                )


