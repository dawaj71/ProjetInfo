#BACKEND
from django.contrib import admin
from django.urls import path

import Backend
from Backend import views

urlpatterns = [
    #path('img_searches', views.reception_image),
    path('img_searches', views.ImageSearch.as_view()),
]
