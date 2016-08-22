# -*- coding: UTF-8 -*-

from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Curso(models.Model):
    nome = models.CharField(max_length=45)
    abreviacao = models.CharField(max_length=45)
    
    def __unicode__(self):
        return unicode(self.nome)
  
    
class Turma(models.Model):
    ano = models.IntegerField()
    numero_turma = models.IntegerField()
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    turno_estudo_orientado = models.CharField(
        max_length=1,
        choices=(("M", "Manhã"),('T', "Tarde"),('N', "Noite"))
        )
    
    def __unicode__(self):
        return str(self.numero_turma) +" "+self.curso.abreviacao


class Periodo(models.Model):
    inicio = models.CharField(max_length=5)
    fim = models.CharField(max_length=5)
    num_periodo = models.IntegerField()
    turno = models.CharField(
        max_length=1,
        choices=(("M", "Manhã"),('T', "Tarde"),('N', "Noite"))
        )
    
    def __unicode__(self):
        return str(self.num_periodo) + "º período da " + self.get_turno_display()
        
        
class Professor(models.Model):
    nome = models.CharField(max_length=45)
    genero = models.CharField(
        max_length=1,
        choices=(('M', 'Masculino'), ('F', 'Feminino'))
        )
    foto = models.ImageField(upload_to='pic_folder/', default='pic_folder/default.jpg')
    
    def __unicode__(self):
        return self.nome
    

class Disciplina(models.Model):
    nome = models.CharField(max_length=45)
    professor = models.ForeignKey(Professor)
    
    def __unicode__(self):
        return self.nome + " (" + self.professor.nome + ")"
        
    
class EstudoOrientado(models.Model):
    dia_da_semana = models.CharField(
        max_length=2,
        choices=(("Se", "Segunda"),("Te", "Terca"),("Qa", "Quarta"),("Qi", "Quinta"),("Sx", "Sexta"))
        )
    periodo = models.ForeignKey(Periodo)
    disciplina = models.ForeignKey(Disciplina)
    turma = models.ForeignKey(Turma)
    
    
    def __unicode__(self):
        return unicode(self.disciplina) + " - " + str(self.turma) + " (" + self.periodo.get_turno_display() + ")"