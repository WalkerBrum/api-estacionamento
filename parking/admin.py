from django.contrib import admin
from . import models

class Parking(admin.ModelAdmin):
    list_display = ['nome_estacionamento', 'logradouro', 'bairro', 'preco_hora', 'total_vagas']
    list_display_links = ['nome_estacionamento']
    search_fields = ['cnpj']


# Register your models here.
admin.site.register(models.Parking)