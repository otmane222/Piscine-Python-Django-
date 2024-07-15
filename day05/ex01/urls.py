from django.urls import path

from .views import ex01_view

urlpatterns = [
    path('', ex01_view, name="ex01")
]
