from django.contrib import admin
from .views import *
from django.urls import path
urlpatterns = [
    path('',home),
    path('verify/',verify_google),
    # path('college/',listColleges)
]
