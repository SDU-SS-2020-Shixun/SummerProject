from django.urls import path
import os

print(os.getcwd())

from . import views

urlpatterns = [
    path('upload', views.upload, name='upload'),
    path('createImg', views.createImg, name='createImg'),
    path('index', views.index, name='index'),
    path('downloadImg', views.downloadImg, name='downloadImg')
]
