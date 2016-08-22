# -*- coding: UTF-8 -*-

from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from django.core import serializers
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.

def api(request):
    # curso = serializers.serialize("json", Curso.objects.all())
    # turma = serializers.serialize("json", Turma.objects.all())
    # periodo = serializers.serialize("json", Periodo.objects.all())
    # professor = serializers.serialize("json", Professor.objects.all())
    # disciplina = serializers.serialize("json", Disciplina.objects.all())
    # estudoOrientado = serializers.serialize("json", EstudoOrientado.objects.all())
    # data = curso + turma + periodo + professor + disciplina + estudoOrientado
    
    diasDaSemana 
    diasDaSemana = ("Se", "Te", "Qa", "Qi", "Sx")
    turmas = Turma.objects.all()
    for turma in turmas:
        for periodo in Periodo.objects.all():
            for dia in diasDaSemana:
                    result = EstudoOrientado.objects.filter(turma=turma, periodo=periodo, dia_da_semana=dia)
                    for eo in result:
                        data.append((str(turma), 
                        (str(periodo.id), str(periodo.num_periodo), periodo.inicio, periodo.fim,
                        (dia, (eo.disciplina, eo.disciplina.professor.nome)))))
                except ObjectDoesNotExist:
                    data.append((str(turma), 
                    (str(periodo.id), str(periodo.num_periodo), periodo.inicio, periodo.fim,
                    (dia, ()))))
    return HttpResponse(data)
    
    
def index(request):
    return render(request, 'tabela.html',
                      {})