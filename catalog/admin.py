from django.contrib import admin
from catalog.models import Pokemon

@admin.register(Pokemon)
class PokemonAdmin(admin.ModelAdmin):
  list_display = ['nombre', 'tipo', 'generacion', 'fecha_creacion']


# Register your models here.
