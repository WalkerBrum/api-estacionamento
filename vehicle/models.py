from email.policy import default
from django.db import models
from user.models import User

# Create your models here.
class Vehicle(models.Model):
    nome_motorista = models.CharField(verbose_name="Nome Motorista", max_length=100)
    idade = models.IntegerField(verbose_name="Idade" )
    user = models.ForeignKey(User, verbose_name="Usuário", on_delete=models.CASCADE)
    placa = models.CharField(verbose_name="Placa", max_length=8,)
    tipo = models.CharField(verbose_name="Tipo", max_length=20,)
    marca = models.CharField(verbose_name="Marca", max_length=20,)
    modelo_veiculo = models.CharField(verbose_name="Modelo veículo", max_length=20, )
    cor = models.CharField(verbose_name="Cor", max_length=20,)
    data_registro = models.DateTimeField(verbose_name="Data Registro", auto_now_add=True)
    data_atualizacao = models.DateTimeField(verbose_name="Data Atualização", auto_now=True)
  
    #on_delete=models.CASCADE
    def __str__(self):
        return self.placa