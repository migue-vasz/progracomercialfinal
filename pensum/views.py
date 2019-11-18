from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.shortcuts import redirect
from .models import Materia, Grado, Asignacion
from .forms import FormMateria, FormGrado

#Materia
def nuevo_grado(request):
    if request.method == "POST":
        form = FormGrado(request.POST)
        if form.is_valid():
            grado = Grado.objects.create(descripcion=form.cleaned_data['descripcion'])
            for materia_id in request.POST.getlist('materias'):
                asignacion = Asignacion(nivel=grado.id, curso=materia_id.id)
                asignacion.save()
            messages.add_message(request, messages.SUCCESS, 'Hecho!')
    else:
        form = FormGrado()
    return render(request, 'pensum/nuevo_grado.html', {'formulario': form})

def listar_grados(request):
    g = Grado.objects.filter().order_by()
    return render(request, 'pensum/listar_grados.html', {'g': g})

def editar_grado(request, pk):
    g = get_object_or_404(Grado, pk=pk)
    if request.method == "POST":
        form = FormGrado(request.POST, instance=g)
        if form.is_valid():
            g = form.save(commit=False)
            g.save()
            return redirect('detalle_grado', pk=g.pk)
    else:
        form = FormGrado(instance=g)
    return render(request, 'pensum/editar_grado.html', {'formulario': form})

def eliminar_grado(request, pk):
    g = get_object_or_404(Grado, pk=pk)
    g.delete()
    return redirect('listar_grados')

def detalle_grado(request, pk):
    g = get_object_or_404(Grado, pk=pk)
    return render(request, 'pensum/detalle_grado.html', {'g': g})
