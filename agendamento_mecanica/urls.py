"""
URL configuration for agendamento_mecanica project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from agendamento.views import home, listagem, novo_agendamento, post_list,signup_view,cadastro,cadastrocarro,meusdados

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name = 'url_listagem'),
    path('nova/', novo_agendamento, name = 'url_novo_agendamento'),
    path('carro/', cadastrocarro, name = 'novo_carro'),
    path('meusdados/', meusdados, name = 'meusdados'),
    path('perfil/', cadastro, name = 'novo_cliente'),
    path('list/', listagem, name = 'post_list'),
    path('signup/', signup_view, name="signup"),
    path("accounts/", include("django.contrib.auth.urls")),
    path('home/', home,name = 'home')
]
