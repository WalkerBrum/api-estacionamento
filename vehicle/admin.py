from django.contrib import admin
from . import models

class Driver(admin.ModelAdmin):
    list_display = ['nome_motorista', 'idade', 'data_registro', 'data_atualizacao', 'placa']
    list_display_links = ['nome_motorista', 'user', 'placa']
    search_fields = ['cpf']


# Register your models here.
admin.site.register(models.Vehicle)

