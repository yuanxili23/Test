import os
from website.lib.database_config import DatabaseConfig


# Statement for enabling the development environment
DEBUG = True

SSL_CONTEXT = 'adhoc'

SQLALCHEMY_TRACK_MODIFICATIONS = False

# Define the application directory
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

APPLICATION_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "website"))

HOST = '0.0.0.0'

PORT = 5000

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://%s:%s@%s/%s' % ('root', 'love0906',
                                                   'localhost', 'sys')

# Secret key for signing cookies
SECRET_KEY = os.urandom(24)
