from django.urls import path

from .views import the_view

urlpatterns = [
    path('', the_view),
]
