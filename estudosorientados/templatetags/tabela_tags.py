from django import template
from estudosorientados.models import *

register = template.Library()

@register.assignment_tag
def getEO(abreviacao, periodo, turma):
    return EstudoOrientado.objects.filter(turma=turma, dia_da_semana=abreviacao, periodo=periodo)


@register.assignment_tag
def getPeriodos(turma):
    return Periodo.objects.filter(turno=turma.turno_estudo_orientado).order_by('turno', 'num_periodo')
