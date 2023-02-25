from django.urls import path, include
from catalog import views
app_name = 'catalogApp'

urlpatterns = [
  path('', views.listPokemon, name="listPokemon"),
]
