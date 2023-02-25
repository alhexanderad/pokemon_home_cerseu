from django.shortcuts import render
from .models import Pokemon

def listPokemon(request):
  lista = Pokemon.objects.all()
  print(lista)
  return render(request, './catalog/pokemon.html', {'lista': lista})