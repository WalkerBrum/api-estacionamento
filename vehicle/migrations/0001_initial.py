# Generated by Django 4.0.1 on 2022-01-22 17:50

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
                ('cpf', models.CharField(max_length=14, unique=True, verbose_name='CPF')),
                ('nome_motorista', models.CharField(max_length=100)),
                ('idade', models.IntegerField()),
                ('placa', models.CharField(max_length=8)),
                ('tipo', models.CharField(max_length=20)),
                ('marca', models.CharField(max_length=20)),
                ('modelo_veiculo', models.CharField(max_length=20, verbose_name='Modelo veículo')),
                ('cor', models.CharField(max_length=20)),
                ('data_registro', models.DateTimeField(auto_now_add=True)),
                ('data_atualizacao', models.DateTimeField(auto_now_add=True, verbose_name='Data atualização')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
            ],
        ),
    ]