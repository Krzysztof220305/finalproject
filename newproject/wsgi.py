import os
from django.core.wsgi import get_wsgi_application

# Upewnij się, że nazwa 'newproject.settings' pasuje do Twojego folderu
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'newproject.settings')

application = get_wsgi_application()