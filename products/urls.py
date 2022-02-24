from django.urls import path
from . import views

#
# /products/1/detail   #info Mosha
# /products/new        #info Mosha

urlpatterns = [
    path('', views.index),
    path('new', views.new)  #dodane do wyświetlenia "New Products" -zapisane w views
]

#2.od P
# urlpatterns = [
#     path('', views.products),
#     path('about', views.productsAbout)
# ]
