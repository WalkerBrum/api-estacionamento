from tabnanny import verbose
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager

# Create your models here.
class User(AbstractUser):
    email = models.EmailField('E-mail', max_length=100, unique=True)
    telefone = models.CharField(null=True, max_length=15, blank=True)
    password = models.CharField('Senha', max_length=100)
    data_registro = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now_add=True, verbose_name="Data atualização")

def __str__(self):
        return self.email

objects = UserManager()

class Meta:
    db_table = 'auth_user'