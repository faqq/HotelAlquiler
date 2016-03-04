from django.contrib import admin
from .models import Cliente #agregar las clases o modelos
# Register your models here.

class UsuarioAdmin(admin.ModelAdmin): #Listar
    list_display = ('ci','nombre','apellido','telefono','genero')
    list_filter = ('genero',)
    search_fields = ('ci',)
#
#fin de la clase

admin.site.register(Cliente, UsuarioAdmin) #nombre de la clase