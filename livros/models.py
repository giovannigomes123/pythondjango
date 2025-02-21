from django.db import models
from uuid import uuid4

# Create your models here.
class Livros(models.Model):
    id_livro=models.UUIDField(primary_key=True, default=uuid4, editable=False)
    titulo = models.CharField(max_length=255)
    autor = models.CharField(max_length=255)
    ano_lancamento=models.IntegerField()
    paginas=models.IntegerField()
    criado_em=models.DateField(auto_now_add=True)
