from django.contrib import admin
from .models import Item  # Importujemy Twój model produktu

admin.site.register(Item)