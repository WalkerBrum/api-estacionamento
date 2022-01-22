from django.contrib import admin

# Register your models here.
from django.contrib import admin
from . import models

class Parking(admin.ModelAdmin):
    list_display = ['nome', 'email', 'data_criacao', 'data_atualizacao']
    list_display_links = ['nome_estacionamento']
    search_fields = ['cnpj']


# Register your models here.
admin.site.register(models.User)