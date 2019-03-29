#BACKEND
from django.contrib import admin
from django.urls import path, re_path


import Backend
from Backend import views

urlpatterns = [
    #path('img_searches', views.reception_image),
    path('img_searches', views.ImageSearch.as_view()),
    re_path(r'^img_searches/(?P<pk>[0-99]+)/?$', views.ImageDetail.as_view()),

]
