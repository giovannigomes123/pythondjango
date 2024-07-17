from rest_framework import viewsets
from api import serializer
from livros import models

class LivrosViewSet(viewsets.ModelViewSet):
    serializer_class=serializer.LivrosSerializer
    queryset=models.Livros.objects.all()