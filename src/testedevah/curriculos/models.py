from django.db import models

from testedevah.pessoas.models import Pessoa


# Create your models here.


class BaseModel(models.Model):
    objects = models.Manager()

    class Meta:
        abstract = True


class Historico_Profissional(BaseModel):
    hist_curriculo = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    nome_empresa = models.TextField(max_length=250, blank=True, null=False)
    duracao_meses = models.IntegerField(blank=True, null=False)
    atribuicoes = models.TextField(max_length=250, blank=True, null=False)
    nome_cargo = models.TextField(max_length=250, blank=True, null=False)


class Formacao(BaseModel):
    form_curriculo = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    FUNDAMENTAL = 'FUN'
    MEDIO = 'MED'
    ESPECIALIZACAO = 'ESP'
    MBA = 'MBA'
    MESTRADO = 'MES'
    DOUTORADO = 'DOU'
    FORMACAO_ESCOLHAS = [
        (FUNDAMENTAL, 'FUNDAMENTAL'),
        (MEDIO, 'MEDIO'),
        (ESPECIALIZACAO, 'ESPECIALIZACAO'),
        (MBA, 'MBA'),
        (MESTRADO, 'MESTRADO'),
        (DOUTORADO, 'DOUTORADO'),
    ]
    CURSANDO = 'CUR'
    CONCLUIDO = 'CON'
    INTERROMPIDO = 'INT'

    SITUACAO_ATUAL_ESCOLHAS = [
        (CURSANDO, 'CURSANDO'),
        (CONCLUIDO, 'CONCLUIDO'),
        (INTERROMPIDO, 'INTERROMPIDO')
    ]

    nome_formacao = models.TextField(max_length=250, blank=True, null=False)
    nome_instituicao = models.TextField(max_length=250, blank=True, null=False)
    duracao_meses = models.IntegerField(blank=True, null=False)
    tipo_formacao = models.CharField(max_length=3, choices=FORMACAO_ESCOLHAS, default='', blank=True, null=False)
    situacao_atual = models.CharField(max_length=3, choices=FORMACAO_ESCOLHAS, default='', blank=True, null=False)


class Curriculo(BaseModel):
    user_curriculo = models.OneToOneField(Pessoa, on_delete=models.CASCADE)
    objetivos = models.TextField(max_length=250, blank=True, null=False)
    resumo = models.TextField(max_length=600, blank=True, null=False)
    cursos_complementares = models.TextField(max_length=500, blank=True, null=False)
    info_complementares = models.TextField(max_length=500, blank=True, null=False)

