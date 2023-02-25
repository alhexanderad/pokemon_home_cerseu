from django.shortcuts import render
from .models import Owner
def owner(request):
  text = 'App Owner funcionando correctamente!!!'
  lista = Owner.objects.all()

  print(lista)

  context ={
    'title': 'Owner',
    'text': text,
    'lista': lista,
  }

  return render(request, './owner/owner.html', context)

def list_owner(request):
  data_context = [
      {
        'nombre': 'Luis I',
        'edad': 25,
        'nacionalidad': 'Mexicana'
      },
      {
        'nombre': 'Maria',
        'edad': 17,
        'nacionalidad': 'Española'
      },
      {
        'nombre': 'Tom',
        'edad': 18,
        'nacionalidad': 'Estadounidense'
      },
      {
        'nombre': 'Ana',
        'edad': 45,
        'nacionalidad': 'Colombiana'
      },
      {
        'nombre': 'Mohammed',
        'edad': 16,
        'nacionalidad': 'Marroquí'
      },
      {
        'nombre': 'Elena',
        'edad': 28,
        'nacionalidad': 'Francesa'
      },
      {
        'nombre': 'Raul',
        'edad': 9,
        'nacionalidad': 'Argentino'
      },
      {
        'nombre': 'Jasmine',
        'edad': 29,
        'nacionalidad': 'Canadiense'
      },
      {
        'nombre': 'Sara',
        'edad': 16,
        'nacionalidad': 'Italiana'
      },
      {
        'nombre': 'Alejandro',
        'edad': 35,
        'nacionalidad': 'Chileno'
      }
  ]

  context = {
    'title': 'Owner List',
    'owners': data_context,
  }
  return render(request, './owner/owner_list.html', context)
