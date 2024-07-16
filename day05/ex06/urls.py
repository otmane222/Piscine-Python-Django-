from django.urls import path

from .views import init, display, populate

urlpatterns = [
    path('init', init, name="init"),
    path('display', display, name="display"),
    # path('update', update, name="update"),
    path('populate', populate, name="populate"),
]
