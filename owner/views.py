from django.shortcuts import render
from .models import  Owner


def owner(request):
  text = "App Owner funcionando correctamente!!!"
  context = {
    'text': text,
    'title': "Owner",
  }
  return render(request, './owner/owner.html', context)


def list_owner(request):
  owners = Owner.objects.all()
  return render(request, './owner/owner_list.html', {'owners': owners})
