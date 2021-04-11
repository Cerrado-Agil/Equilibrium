from django.db import models
from django.contrib.auth.models import AbstractUser

class User(models.Model):
    nome = models.CharField(max_length=50)
    sobreNome = models.CharField(max_length=50)
    dataNasc = models.DateField()
    cpf = models.CharField(max_length=11, unique=True)
    email = models.CharField(max_length=60, unique=True, blank=True)
    dataCadastro = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.nome + ' ' + self.sobreNome + ' - ' + self.cpf


