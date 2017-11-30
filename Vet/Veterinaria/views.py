from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, View
from django.urls import reverse_lazy

from .models import Mascota
# Create your views here.

class PetList(ListView):
    ListView.model = Mascota

# TODO hacer que después de cada create se vaya a la página de detalles
class PetCreate(CreateView):
    CreateView.model = Mascota
    CreateView.fields = ['name', 'date_of_birth']
    CreateView.success_url = reverse_lazy("url_list_pets")

class PetDetails(DetailView):
    DetailView.model = Mascota
    DetailView.context_object_name = 'mascota'