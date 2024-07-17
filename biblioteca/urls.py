from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from api import viewset as livrosviewsets

route = routers.DefaultRouter()
route.register(r'books', livrosviewsets.LivrosViewSet, basename='Livros')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(route.urls))
]
