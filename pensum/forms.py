from django import forms
from .models import Materia, Grado

class FormMateria(forms.ModelForm):
    class Meta:
        model = Materia
        fields = ('descripcion','nota')

class FormGrado(forms.ModelForm):
    class Meta:
        model = Grado
        fields = ('descripcion','materias')
