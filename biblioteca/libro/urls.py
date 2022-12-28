from django.urls import path 
from . import views

urlpatterns = [
    path('crearlibro/', views.crearLibro, name='crearLibro'),
    path('libros/', views.libros, name='libros'),
    path('libros/deseos/', views.listaDeseos, name='listaDeseos'),
    path('buscar/libro/', views.busacarLibros, name='buscarLibros'),
    path('descripcion/libro/<int:id>/', views.descripcionLibro, name='descripcionLibro'),
    path('agregarCarro/libro/<int:id>/', views.agregarCarro, name='agregarCarro'),
    path('libro/agregarResena/<int:id>/', views.agregarResena, name='agregarResena'),
    path('libros/deseos/<int:id>', views.agregarDeseos, name='agregarDeseos'),
    path('libros/deseos/eliminar/<int:id>', views.quitarLibroDeseo, name='quitarLibroDeseo')
]