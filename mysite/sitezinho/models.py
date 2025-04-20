# models.py (versão corrigida)
from django.db import models
from django.contrib.auth.models import User

class PerfilUsuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True)
    telefone = models.CharField(max_length=15, blank=True, null=True)
    def __str__(self):
        return self.user.username

# (Remova a classe TesteInvasao completamente)

class Funcionarios(models.Model):
    nome = models.CharField(max_length=30, blank=False, null=False)
    numero = models.IntegerField()
    ponto = models.DateField()
    email = models.EmailField(max_length=254)
    def __str__(self):
        return str(self.numero)

class Gerente(models.Model):
    nome = models.CharField(max_length=50)
    horario = models.IntegerField()
    email = models.EmailField(max_length=254)
    numero_comercial = models.IntegerField()
    def __str__(self):
        return self.nome