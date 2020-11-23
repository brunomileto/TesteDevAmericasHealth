from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from testedevah.pessoas.models import Pessoa


class SignUpForm(UserCreationForm):
    cpf = forms.CharField(max_length=120, required=True)
    data_nascimento = forms.DateField(required=True)
    cidade = forms.CharField(max_length=30, required=True)
    estado = forms.CharField(max_length=2, required=True)
    email = forms.CharField(max_length=30, required=True)

    class Meta:
        model = User
        fields = ('username', 'cpf', 'data_nascimento', 'cidade', 'estado', 'estado', 'first_name', 'last_name',  'email',
                  'password1', 'password2', )
