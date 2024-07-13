from django.urls import path

from .views import ex00_view

urlpatterns = [
    path('init', ex00_view, name='init')
]
