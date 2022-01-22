from email.policy import default
from django.db import models
from user.models import User

# Create your models here.
class Vehicle(models.Model):
    cpf = models.CharField("CPF", max_length=14, unique=True)
    nome_motorista = models.CharField(max_length=100)
    idade = models.IntegerField()
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Usuário")
    placa = models.CharField( max_length=8,)
    tipo = models.CharField( max_length=20,)
    marca = models.CharField( max_length=20,)
    modelo_veiculo = models.CharField(max_length=20, verbose_name="Modelo veículo",)
    cor = models.CharField(max_length=20,)
    data_registro = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now_add=True, verbose_name="Data atualização")
  

    def __str__(self):
        return self.placa