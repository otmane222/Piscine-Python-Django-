from django.urls import path

from .views import display, populate, update

urlpatterns = [
    path('display', display, name="display"),
    path('update', update, name="update"),
    path('populate', populate, name="populate"),
]
