# Generated by Django 4.0.1 on 2022-01-26 05:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_motorista', models.CharField(max_length=100, verbose_name='Nome Motorista')),
                ('idade', models.IntegerField(verbose_name='Idade')),
                ('placa', models.CharField(max_length=8, verbose_name='Placa')),
                ('tipo', models.CharField(max_length=20, verbose_name='Tipo')),
                ('marca', models.CharField(max_length=20, verbose_name='Marca')),
                ('modelo_veiculo', models.CharField(max_length=20, verbose_name='Modelo veículo')),
                ('cor', models.CharField(max_length=20, verbose_name='Cor')),
                ('data_registro', models.DateTimeField(auto_now_add=True, verbose_name='Data Registro')),
                ('data_atualizacao', models.DateTimeField(auto_now=True, verbose_name='Data Atualização')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
            ],
        ),
    ]
