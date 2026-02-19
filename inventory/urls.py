from django.urls import path
from . import views

urlpatterns = [
    # To kieruje bezpośrednio do Twojej listy produktów
    path('', views.item_list, name='item_list'),
]