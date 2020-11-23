from django.db import models
from testedevah.pessoas.models import Pessoa
# Create your models here.


class Vaga(models.Model):
    usuarios_cadastrados = models.ManyToManyField(Pessoa)
    nome_vaga = models.TextField(max_length=250, blank=True, null=False)
    nome_empresa = models.TextField(max_length=250, blank=True, null=False)
    tipo_vaga = models.TextField(max_length=250, blank=True, null=False)
    salario = models.TextField(max_length=250, blank=True, null=False)
    beneficios = models.TextField(max_length=250, blank=True, null=False)
    descricao = models.TextField(max_length=250, blank=True, null=False)
    requisitos = models.TextField(max_length=250, blank=True, null=False)
    filme_relacionado = models.TextField(max_length=250, blank=True, null=False)


