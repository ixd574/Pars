import os
import sys

# Add the project root to Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from app.app import app as flask_app

def handler(environ, start_response):
    return flask_app(environ, start_response)
