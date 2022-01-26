from django.contrib import admin
from .models import Parking

class ParkingAdmin(admin.ModelAdmin):
    list_display = ['nome_estacionamento', 'logradouro', 'bairro', 'preco_hora', 'total_vagas']
    list_display_links = ['nome_estacionamento']
    search_fields = ['nome_estacionamento', 'cnpj']


# Register your models here.
admin.site.register(Parking, ParkingAdmin)