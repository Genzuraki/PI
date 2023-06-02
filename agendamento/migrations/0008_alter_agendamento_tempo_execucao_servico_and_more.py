# Generated by Django 4.2.1 on 2023-06-02 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agendamento', '0007_alter_resumo_servico_cliente_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agendamento',
            name='tempo_execucao_servico',
            field=models.CharField(default='avaliando', max_length=45),
        ),
        migrations.AlterField(
            model_name='cadastro_cliente',
            name='cpf',
            field=models.CharField(max_length=11, verbose_name='cpf'),
        ),
        migrations.AlterField(
            model_name='cadastro_cliente',
            name='nome',
            field=models.CharField(max_length=255, verbose_name='nome'),
        ),
        migrations.AlterField(
            model_name='cadastro_cliente',
            name='sexo',
            field=models.CharField(max_length=1, verbose_name='sexo'),
        ),
    ]
