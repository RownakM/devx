from django.contrib import admin
from .views import *
from django.urls import path
urlpatterns = [
    path('',home),
    path('verify/',verify_google),
    path('application/submit/',application)
    # path('mail/',sendMail)
    # path('college/',listColleges)
]
