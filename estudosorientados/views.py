# -*- coding: UTF-8 -*-

import os
import base64
from django.conf import settings

from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from django.core import serializers
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.

def curso_api(request):
    curso = serializers.serialize("json", Curso.objects.all())
    return HttpResponse(curso)
    
    
def turma_api(request):
    turma = serializers.serialize("json", Turma.objects.all())
    return HttpResponse(turma)    


def periodo_api(request):
    periodo = serializers.serialize("json", Periodo.objects.all())
    return HttpResponse(periodo)


def professor_api(request):
    professor = serializers.serialize("json", Professor.objects.all())
    return HttpResponse(professor)

def imagem_api(request, professor):
    url = Professor.objects.get(id=int(professor)).foto.url
    filename = os.path.join(settings.BASE_DIR, url)
    with open(filename, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    return HttpResponse(encoded_string)
    

def disciplina_api(request):
    disciplina = serializers.serialize("json", Disciplina.objects.all())
    return HttpResponse(disciplina)

def estudoOrientado_api(request):
    estudoOrientado = serializers.serialize("json", EstudoOrientado.objects.all())
    return HttpResponse(estudoOrientado)
    
    
def index(request):
    diasDaSemana = (("Se", "Segunda"),("Te", "Terça"),("Qa", "Quarta"),("Qi", "Quinta"),("Sx", "Sexta"))
    turmas = Turma.objects.all().order_by('ano', 'numero_turma', 'curso')
    return render(request, 'tabela.html',
                      {"diasDaSemana" : diasDaSemana,
                      "turmas" : turmas,
                          
                      })