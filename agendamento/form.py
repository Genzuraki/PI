from django.forms import ModelForm
from .models import Agendamento
from .models import Cadastro_Cliente
from .models import Cadastro_Carro

class AgendamentoForm(ModelForm):
    class Meta:
        model = Agendamento
        fields = ['cliente','descricao','data_entrada']

class ClientForm(ModelForm):
    class Meta:
        model = Cadastro_Cliente
        fields = ['nome','sexo','cpf']

class CarroForm(ModelForm):
    class Meta:
        model = Cadastro_Carro
        fields = ['cliente','placa_veiculo','fabricante','modelo','ano_fabricacao']