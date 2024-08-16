from django.contrib import admin
from django.urls import path, include
from .views import shorten

urlpatterns = [
    path("",shorten),

]
