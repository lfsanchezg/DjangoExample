from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView

from .models import Mascota, Duegno

# Vistas de clase

class PetList(ListView):
    model = Mascota

class PetCreate(CreateView):
    model = Mascota
    fields = '__all__'

class PetDetails(DetailView):
    model = Mascota
    context_object_name = 'mascota'

class DuegnoCreate(CreateView):
    model = Duegno
    fields = '__all__'

# Vistas básicas

def owner_list(request):
    # Vista básica, hola mundo
    return HttpResponse("asdasd")

def owner_list2(request):
    # Vista básica, crea una lista de objetos y los representa sobre el template mascota_list

    objetos = [
        {
            'id': 1,
            'name': 'dueño 1'
        },
        {
            'id': 1,
            'name': 'dueño 2'
        },
        {
            'id': 1,
            'name': 'dueño 3'
        },
        {
            'id': 1,
            'name': 'dueño 4'
        },
    ]

    return render(request, 'Veterinaria/mascota_list.html', context={'mascota_list': objetos})

def owner_list3(request):
    # Vista básica, obtiene todos los dueños de la bd,
    # genera una lista y los pasa a la template de mascotas

    duegnos = Duegno.objects.all()

    return render(request, 'Veterinaria/mascota_list.html', context={'mascota_list': duegnos})

def owner_list4(request):
    # Vista básica, hace una consulta sobre la bd, generando una lista
    # y la pasa al template de mascotas.

    duegnos = Duegno.objects.filter(age__gte=30, name__contains='P')

    return render(request, 'Veterinaria/mascota_list.html', context={'mascota_list': duegnos})

def owner_detail(request):

    #recibiendo param por get params:
    idDuegno = request.GET.get('identificador')

    duegno_bd = Duegno.objects.get(pk=idDuegno)

    mascotas = Mascota.objects.filter(duegno=duegno_bd)

    diccionarioContextoCreadoAparte = dict()
    diccionarioContextoCreadoAparte['duegno_plantilla'] = duegno_bd
    diccionarioContextoCreadoAparte['sus_mascotas'] = mascotas

    return render(request, 'Veterinaria/duegno_detail.html', context=diccionarioContextoCreadoAparte)

