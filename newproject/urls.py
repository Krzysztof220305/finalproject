from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# Najpierw definiujemy listę urlpatterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('inventory.urls')),
]

# Dopiero POTEM sprawdzamy DEBUG i dodajemy obsługę plików media
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)