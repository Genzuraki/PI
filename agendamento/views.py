from django.shortcuts import redirect, render
from .models import  Agendamento, Cadastro_Cliente, Cadastro_Carro
from .form import AgendamentoForm, ClientForm, CarroForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
from django.http import HttpResponse
import datetime


def home(request):
    data = {}
    data['transacoes'] = ['t1','t2','t3',]
    data['now'] = datetime.datetime.now()

    ##now = datetime.datetime.now()
    ##html = "<html><body>It is now %s.</body></html>" % now
    return render(request,'agendamento/home.html',data)
    #return HttpResponse(html)

def listagem(request):
    data = {}
    data['agendamento'] = Agendamento.objects.all()
    return render(request,'agendamento/listagem.html',data)

def novo_agendamento(request):
    data = {}
    form = AgendamentoForm(request.POST or None)
    
    if form.is_valid():
        form.save()
        return listagem(request)

    data['form'] = form
    return render(request, 'agendamento/form.html', data)

def post_list(request):
    data = {}
    data['transacoes'] = ['t1','t2','t3',]
    data['now'] = datetime.datetime.now()

    return render(request,'agendamento/list.html',data)

def signup_view(request):
    form = UserCreationForm(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('novo_cliente')
    return render(request, 'agendamento/signup.html', {'form': form})

def cadastrocarro(request):
    data = {}
    form = CarroForm(request.POST or None)
    
    if form.is_valid():
        form.save()
        return home(request)
    
    data['form'] = form
    data['url'] = '/list/'
    return render(request, 'agendamento/form.html', data)

def cadastro(request):
    data = {}
    form = ClientForm(request.POST or None)
    
    if form.is_valid():
        form.save()
        return redirect('novo_carro')

    data['form'] = form
    data['url'] = '/list/'
    return render(request, 'agendamento/form.html', data)

def meusdados(request):
    data = {}
    data['meusdados'] = Cadastro_Cliente.objects.all()
    data['meuveiculo'] = Cadastro_Carro.objects.all()
    return render(request,'agendamento/meusdados.html',data)