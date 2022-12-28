from django.urls import path
from . import views

urlpatterns = [
    path('carro/', views.carro, name='carro'),
    path('carro/actualizar',  views.actualizar, name='actualizar'),
    path('carro/eliminarArticulo/<int:id>', views.eliminarArticulo, name='eliminarArticulo'),
    path('carro/realizarCompra/', views.realizarCompra, name='realizarCompra')
]