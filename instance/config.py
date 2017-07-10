
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DEBUG= os.environ.get('SECRET_KEY')
CSRF_ENABLED = os.environ.get('CSRF_ENABLED')
SECRET_KEY = os.environ.get('SECRET_KEY')
FROM_EMAIL = os.environ.get('FROM_EMAIL')
FROM_PASSWORD = os.environ.get('FROM_PASSWORD')
TO_EMAIL = os.environ.get('TO_EMAIL')
