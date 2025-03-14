"""
URL configuration for d04 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('ex00/', include('ex00.urls'), name="ex00"),
    path('ex01/', include('ex01.urls'), name="ex01"),
    path('ex02/', include('ex02.urls'), name="ex02"),
    path('ex03/', include('ex03.urls'), name="ex03"),
    path('ex04/', include('ex04.urls'), name="ex04"),
    path('ex05/', include('ex05.urls'), name="ex05"),
    path('ex06/', include('ex06.urls'), name="ex06"),
    path('ex07/', include('ex07.urls'), name="ex07"),
    path('ex08/', include('ex08.urls'), name="ex08"),
    path('ex09/', include('ex09.urls'), name="ex09"),
    path('ex10/', include('ex10.urls'), name="ex10"),
    path('admin/', admin.site.urls),
]
