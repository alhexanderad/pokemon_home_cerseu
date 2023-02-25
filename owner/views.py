from django.shortcuts import render
from .models import  Owner

def list_owner(request):
  owners = Owner.objects.all()
  return render(request, './owner/owner_list.html', {'owners': owners})
