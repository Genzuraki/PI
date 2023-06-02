# Generated by Django 4.2.1 on 2023-05-18 16:05

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cadastro_Carro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('placa_veiculo', models.CharField(max_length=7)),
                ('fabricante', models.CharField(max_length=50)),
                ('modelo', models.CharField(max_length=20)),
                ('ano_fabricacao', models.IntegerField(validators=[django.core.validators.MaxValueValidator(2023), django.core.validators.MinValueValidator(1884)])),
                ('dt_criacao', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cadastro_Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('sexo', models.CharField(max_length=1)),
                ('cpf', models.CharField(max_length=11)),
                ('dt_criacao', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Resumo_Servico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_saida', models.DateField()),
                ('tempo_execucao_servico', models.CharField(max_length=45)),
                ('valor_pago', models.DecimalField(decimal_places=2, max_digits=7)),
                ('tempo_garantia', models.CharField(max_length=45)),
                ('cliente', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='agendamento.cadastro_cliente')),
                ('placa_veiculo', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='agendamento.cadastro_carro')),
            ],
        ),
        migrations.CreateModel(
            name='Cadastro_Endereco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rua', models.CharField(max_length=200)),
                ('numero', models.CharField(max_length=10)),
                ('bairro', models.CharField(max_length=30)),
                ('cidade', models.CharField(max_length=30)),
                ('estado', models.CharField(max_length=30)),
                ('pais', models.CharField(max_length=30)),
                ('dt_criacao', models.DateTimeField(auto_now_add=True)),
                ('cliente', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='agendamento.cadastro_cliente')),
            ],
        ),
        migrations.AddField(
            model_name='cadastro_carro',
            name='cliente',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='agendamento.cadastro_cliente'),
        ),
        migrations.CreateModel(
            name='Agendamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=255)),
                ('data_entrada', models.DateField()),
                ('tempo_execucao_servico', models.CharField(max_length=45)),
                ('cliente', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='agendamento.cadastro_cliente')),
            ],
        ),
    ]