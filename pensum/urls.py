from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_grados, name='listar_grados'),
    path('grado/nuevo', views.nuevo_grado, name='nuevo_grado'),
    path('grado/<int:pk>/editar/', views.editar_grado, name='editar_grado'),
    path('grado/<pk>/eliminar/', views.eliminar_grado, name='eliminar_grado'),
    path('grado/<int:pk>/', views.detalle_grado, name='detalle_grado'),
]
