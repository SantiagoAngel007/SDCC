from django.contrib import admin

# Register your models here.
from .models import Maquina,Encargado,Emisor,Evaluador,Actividades

admin.site.register(Encargado)
admin.site.register(Maquina)
admin.site.register(Emisor)
admin.site.register(Evaluador)
admin.site.register(Actividades)

