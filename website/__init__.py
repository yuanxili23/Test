from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import timedelta

app = Flask(__name__)

app.config.from_object('config')
db = SQLAlchemy(app)
db.create_all()

import website.views.views
import website.views.errors

