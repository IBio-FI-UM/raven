from django.contrib import admin

# Register your models here.

from .models import Imagen,Pregunta,Codigo


admin.site.register(Imagen)

admin.site.register(Pregunta)
admin.site.register(Codigo)

