# Register your models here.
from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ['email', 'telefone', 'data_registro', 'data_atualizacao']
    list_display_links = ['email',  'telefone']
    search_fields = ['email']


# Register your models here.
admin.site.register(User, UserAdmin)