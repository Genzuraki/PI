from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
import datetime

class Cadastro_Cliente(models.Model):
    nome = models.CharField(max_length=255, verbose_name="nome")
    sexo = models.CharField(max_length=1, verbose_name="sexo")
    cpf = models.CharField(max_length=11, verbose_name="cpf")
    #salario = models.DecimalField(max_digits=7,decimal_places=2,default=None, blank=True, null=True)
    dt_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

class Cadastro_Carro(models.Model):
    cliente = models.ForeignKey(Cadastro_Cliente, on_delete=models.CASCADE,default=None,related_name='cliente')
    placa_veiculo = models.CharField(max_length=7)
    fabricante = models.CharField(max_length=50)
    modelo = models.CharField(max_length=20)
    ano_fabricacao = models.IntegerField(validators = [MaxValueValidator(int(datetime.date.today().year)),MinValueValidator(1884),])
    dt_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
       return self.placa_veiculo
    
class Cadastro_Endereco(models.Model):
    cliente = models.ForeignKey(Cadastro_Cliente, on_delete=models.CASCADE,default=None)
    rua = models.CharField(max_length=200)
    numero = models.CharField(max_length=10)
    bairro = models.CharField(max_length=30)
    cidade = models.CharField(max_length=30)
    estado = models.CharField(max_length=30)
    pais = models.CharField(max_length=30)
    #salario = models.DecimalField(max_digits=7,decimal_places=2,default=None, blank=True, null=True)
    dt_criacao = models.DateTimeField(auto_now_add=True)

class Agendamento(models.Model):
    cliente = models.ForeignKey(Cadastro_Cliente, on_delete=models.CASCADE,default=None)
    descricao = models.CharField(max_length=255)    
    data_entrada = models.DateField()
    tempo_execucao_servico = models.CharField(max_length=45,default='avaliando')  
    #descricao = models.CharField(max_length=255)    
    
    def __str__(self):
        return self.descricao


class Resumo_Servico(models.Model):
    cliente = models.ForeignKey(Cadastro_Cliente, on_delete=models.CASCADE,default=None)
    placa_veiculo = models.ForeignKey(Cadastro_Carro, on_delete=models.CASCADE,default=None)
    data_saida = models.DateField()
    tempo_execucao_servico = models.CharField(max_length=45)  
    valor_pago = models.DecimalField(max_digits=7,decimal_places=2)
    tempo_garantia = models.CharField(max_length=45)      

