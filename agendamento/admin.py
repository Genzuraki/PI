from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Cadastro_Cliente)
admin.site.register(Cadastro_Endereco)
admin.site.register(Cadastro_Carro)
admin.site.register(Agendamento)
admin.site.register(Resumo_Servico)