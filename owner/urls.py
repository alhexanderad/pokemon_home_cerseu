from django.urls import path, include
from owner import views
app_name = 'owner'

urlpatterns = [
  path('lista/', views.list_owner, name="ListOwner"),
]
