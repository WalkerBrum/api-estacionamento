from django.contrib import admin
from .models import Vehicle

class VehicleAdmin(admin.ModelAdmin):
    list_display = ['nome_motorista', 'user', 'placa', 'data_registro', 'data_atualizacao', ]
    list_display_links = ['nome_motorista', 'user', 'placa']
    search_fields = ['nome_motorista', 'placa']


# Register your models here.
admin.site.register(Vehicle, VehicleAdmin)

