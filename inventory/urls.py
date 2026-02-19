from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls), # Tu powinny być .urls
    path('', include('inventory.urls')),
]

# Dodaj to, aby Azure wiedział jak serwować zdjęcia w trybie DEBUG
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)