from flask import Flask

app = Flask(__name__)

app.config.from_object('config')

import website.views.views
import website.views.errors



