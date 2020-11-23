from django import forms
from testedevah.curriculos.models import Curriculo, Historico_Profissional, Formacao


class CurriculoForm(forms.ModelForm):
    objetivos = forms.CharField(widget=forms.Textarea, max_length=250, required=True)
    resumo = forms.CharField(widget=forms.Textarea, max_length=600, required=True)
    cursos_complementares = forms.CharField(widget=forms.Textarea, max_length=500, required=True)
    info_complementares = forms.CharField(widget=forms.Textarea, max_length=500, required=True)

    class Meta:
        model = Curriculo
        fields = ('objetivos', 'resumo', 'cursos_complementares', 'info_complementares', )


class Historico_ProfissionalForm(forms.ModelForm):
    nome_empresa = forms.CharField(widget=forms.Textarea, max_length=250, required=True)
    atribuicoes = forms.CharField(widget=forms.Textarea, max_length=250, required=True)
    duracao_meses = forms.IntegerField(required=True)
    nome_cargo = forms.CharField(widget=forms.Textarea, max_length=250, required=True)

    class Meta:
        model = Curriculo
        fields = ('nome_empresa', 'duracao_meses', 'nome_cargo', 'atribuicoes', )


class FormacaoForm(forms.ModelForm):
    nome_formacao = forms.CharField(widget=forms.Textarea, max_length=250, required=True)
    nome_instituicao = forms.CharField(widget=forms.Textarea, max_length=250, required=True)
    duracao_meses = forms.IntegerField(required=True)
    tipo_formacao = forms.CharField(required=True)
    situacao_atual = forms.CharField(required=True)

    class Meta:
        model = Curriculo
        fields = ('nome_formacao', 'tipo_formacao', 'nome_instituicao', 'situacao_atual', 'duracao_meses')

