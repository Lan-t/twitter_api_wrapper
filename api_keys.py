import os

API_KEY = os.environ.get('TWITTER_API_KEY')
API_SECRET_KEY = os.environ.get('TWITTER_API_KEY_SECRET')
ORIGIN = os.environ.get('API_ORIGIN')
BASE_PATH = os.environ.get('API_BASE_PATH')
BASE_URL = 'http://' + ORIGIN + (BASE_PATH or '')
TO_PATH = os.environ.get('API_TO_PATH') or '/entry'
DEBUG = os.environ.get('DEBUG') == 'true'
