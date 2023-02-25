from django.urls import path, include
from owner import views
app_name = 'ownerApp'

urlpatterns = [
  path('', views.owner, name="Owner"),
  path('lista/', views.list_owner, name="ListOwner"),
]
