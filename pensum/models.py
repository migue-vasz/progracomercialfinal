from django.db import models
from django.contrib import admin

class Materia(models.Model):
    descripcion = models.CharField(max_length=50)
    nota        = models.IntegerField()
    def __str__(self):
        return self.descripcion

class Grado(models.Model):
    descripcion = models.CharField(max_length=100)
    materias    = models.ManyToManyField(Materia, through='Asignacion')
    def __str__(self):
        return self.descripcion

class Asignacion (models.Model):
    nivel = models.ForeignKey(Grado, on_delete=models.CASCADE)
    curso = models.ForeignKey(Materia, on_delete=models.CASCADE)

class AsignacionInLine(admin.TabularInline):
    model = Asignacion
    extra = 1

class MateriaAdmin(admin.ModelAdmin):
    inlines = (AsignacionInLine,)

class GradoAdmin (admin.ModelAdmin):
    inlines = (AsignacionInLine,)
