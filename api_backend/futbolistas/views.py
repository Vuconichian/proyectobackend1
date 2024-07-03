from django.http import JsonResponse
from django.shortcuts import render
from futbolistas.models import Futbolista, Director, Estadio
from futbolistas.serializers import FutbolistaSerializer, DirectorSerializer, EstadioSerializer
from django.views.generic import CreateView
from futbolistas.forms import FutbolistaForm, DirectorForm, UserForm, EstadioForm
# Create your views here.

def get_all_futbolistas():
    futbolistas = Futbolista.objects.all().order_by('name')
    futbolistas_serializers = FutbolistaSerializer(futbolistas, many=True)
    return futbolistas_serializers.data

def get_all_directors():
    directors = Director.objects.all().order_by('name')
    directors_serializers = DirectorSerializer(directors, many=True)
    return directors_serializers.data

def get_all_estadios():
    estadios = Estadio.objects.all().order_by('name')
    estadios_serializers = EstadioSerializer(estadios, many=True)
    return estadios_serializers.data

def futbolistas_rest(request):
    futbolistas = get_all_futbolistas()
    return JsonResponse(futbolistas, safe=False)

def directors_rest(request):
    directors = get_all_directors()
    return JsonResponse(directors, safe=False)

def estadios_rest(request):
    estadios = get_all_estadios()
    return JsonResponse(estadios, safe=False)

def index_pil(request):
    futbolistas = get_all_futbolistas()
    directors = get_all_directors()
    estadios = get_all_estadios()
    return render(request, 'index_pil.html', {'futbolistas': futbolistas, 'directors': directors, 'estadios': estadios})

def users_rest(request):
    return JsonResponse("Ok", safe=False)

class NewFutbolistaView(CreateView):
    form_class = FutbolistaForm
    template_name = 'form_fut.html'
    success_url = '/'

class NewDirectorView(CreateView):
    form_class = DirectorForm
    template_name = 'form_dir.html'
    success_url = '/'

class NewEstadioView(CreateView):
    form_class = EstadioForm
    template_name = 'form_est.html'
    success_url = '/'

class NewUserView(CreateView):
    form_class = UserForm
    template_name = 'form_usu.html'
    success_url = '/'
