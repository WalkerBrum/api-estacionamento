from tabnanny import verbose
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(verbose_name="E-mail", max_length=100, unique=True)
    telefone = models.CharField(verbose_name="Telefone", null=True, max_length=15, blank=True)   
    data_registro = models.DateTimeField(verbose_name="Data Registro", auto_now_add=True)
    data_atualizacao = models.DateTimeField(verbose_name="Data Atualização", auto_now=True)
def __str__(self):
        return self.email

objects = UserManager()

class Meta:
    db_table = 'auth_user'