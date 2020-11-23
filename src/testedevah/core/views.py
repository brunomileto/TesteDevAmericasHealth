from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render
from testedevah.pessoas.form import SignUpForm
from testedevah.curriculos.form import CurriculoForm, FormacaoForm, Historico_ProfissionalForm

# Create your views here.


def home(request):
    return render(request, 'home.html')


@login_required
def user_homepage(request):
    data = User.objects.all()
    context = {'data': data}
    return render(request, 'user_homepage.html', context)


def signup(request):
    msg = []
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # Carrega a instância da pessoa salva pelo sinal
            user.pessoa.cidade = form.cleaned_data.get('cidade')
            user.pessoa.cpf = form.cleaned_data.get('cpf')
            user.pessoa.data_nascimento = form.cleaned_data.get('data_nascimento')
            user.pessoa.cidade = form.cleaned_data.get('cidade')
            user.pessoa.estado = form.cleaned_data.get('estado')
            user.pessoa.nome = form.cleaned_data.get('nome')
            user.pessoa.sobrenome = form.cleaned_data.get('sobrenome')
            user.pessoa.email = form.cleaned_data.get('email')
            user.save()
            senha = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=senha)
            login(request, user)
            return render(request, 'home.html')
        else:
            error = form.errors.as_data()
            for key in error:
                for index in range(len(error[key])):
                    validation_error = list(error[key][index])[0]
                    msg.append(validation_error)
            return render(request, 'registration/signup.html', {'form': form,
                                                                'msg': msg})
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form,
                                                        'msg': msg})


@login_required(redirect_field_name='home')
def curriculo_view(request):
    msg = []
    curriculo_form = CurriculoForm()
    if request.method == 'POST':
        curriculo_form = CurriculoForm(request.POST, instance=request.user.pessoa)
    if curriculo_form.is_valid():
        curriculo = curriculo_form.save()
        curriculo.user_curriculo = request.user.pessoa
        curriculo.resumo = curriculo_form.cleaned_data.get('resumo')
        curriculo.cursos_complementares = curriculo_form.cleaned_data.get('cursos_complementares')
        curriculo.info_complementares = curriculo_form.cleaned_data.get('info_complementares')
        curriculo.objetivos = curriculo_form.cleaned_data.get('objetivos')
        curriculo.save()
        return render(request, 'home.html')
    else:
        error_curriculo = curriculo_form.errors.as_data()
        for key in error_curriculo:
            for index in range(len(error_curriculo[key])):
                validation_error = list(error_curriculo[key][index])[0]
                msg.append(validation_error)
        return render(request, 'curriculo/curriculo_template.html', {'form': curriculo_form,
                                                            'msg': msg})


@login_required(redirect_field_name='home')
def formacao_view(request):
    msg = []
    formacao_form = FormacaoForm()
    if request.method == 'POST':
        formacao_form = FormacaoForm(request.POST)
    if formacao_form.is_valid():
        pass
    else:
        error_formacao = formacao_form.errors.as_data()
        for key2 in error_formacao:
            for index in range(len(error_formacao[key2])):
                validation_error = list(error_formacao[key2][index])[0]
                msg.append(validation_error)
        return render(request, 'curriculo/formacao_template.html', {'form': formacao_form,
                                                            'msg': msg})



@login_required(redirect_field_name='home')
def historico_view(request):
    msg = []
    historico_profissional_form = Historico_ProfissionalForm()
    if request.method == 'POST':
        historico_profissional_form = Historico_ProfissionalForm(request.POST)
    if historico_profissional_form.is_valid():
        pass
    else:
        error_historico = historico_profissional_form.errors.as_data()
        for key1 in error_historico:
            for index in range(len(error_historico[key1])):
                validation_error = list(error_historico[key1][index])[0]
                msg.append(validation_error)
        return render(request, 'curriculo/historico_template.html', {'form': historico_profissional_form,
                                                            'msg': msg})
