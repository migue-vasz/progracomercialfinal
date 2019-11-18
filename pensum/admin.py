from django.contrib import admin
from pensum.models import Grado, GradoAdmin, Materia, MateriaAdmin

admin.site.register(Grado, GradoAdmin)
admin.site.register(Materia, MateriaAdmin)
