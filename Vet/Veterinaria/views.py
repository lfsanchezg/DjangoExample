from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Mascota, Duegno

# Vistas de clase

def homeView(request):
    return HttpResponseRedirect(reverse("url_list_pets"))

class PetList(ListView):
    model = Mascota

class PetCreate(CreateView):
    model = Mascota
    fields = '__all__'

class PetDetails(DetailView):
    model = Mascota
    context_object_name = 'mascota'

class DuegnoCreate(LoginRequiredMixin, CreateView):
    model = Duegno
    fields = '__all__'

    def get_success_url(self):
        return reverse("duegno_list_view")


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

@login_required()
def owner_detail(request, duegno_id):

    if duegno_id is None:
        return HttpResponse("""Necesito el parámetro get "identificador" """)

    duegno_bd = Duegno.objects.get(pk=duegno_id)

    mascotas = Mascota.objects.filter(duegno=duegno_bd)

    diccionarioContextoCreadoAparte = dict()
    diccionarioContextoCreadoAparte['duegno_plantilla'] = duegno_bd
    diccionarioContextoCreadoAparte['sus_mascotas'] = mascotas

    return render(request, 'Veterinaria/duegno_detail.html', context=diccionarioContextoCreadoAparte)

def duegno_list(request):

    duegnos = Duegno.objects.all()

    def get_numero_de_mascotas(duegno: Duegno):
        return len(Mascota.objects.filter(duegno=duegno)) # sí, funciona

    lista_para_la_template = [{'id_duegno': duegno.id, 'nombre_duegno': str(duegno), 'n_mascotas': get_numero_de_mascotas(duegno)} for duegno in duegnos]

    return render(request, 'Veterinaria/duegno_list.html', context={'lista_de_duegnos': lista_para_la_template})