from django.urls import path

from .views import templates, django, display

urlpatterns = [
    path('django/', django, name='index'),
    path('display/', display, name='display'),
    path('templates/', templates, name='temple'),
]