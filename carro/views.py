from django.shortcuts import render, redirect
import requests

mensaje = None
error = False
# Create your views here.
def carro(request):
    global mensaje
    global error
    
    try:
        libros = requests.get(
        'http://127.0.0.1:5000/biblioteca/articulos/carro').json()
        #valor total de los articulos en el carro
        total = 0

        for libro in libros['data']:
            #calcula el total de cada articulo
            libro['subtotal'] = libro['cantidad'] * libro['libro']['valor']
            total = total + libro['subtotal']
        # agrega el total de los articulos al diccionario
        libros['total'] = total
        
        contexto = {
            'libros': libros['data'],
            'total': libros['total'],
            'mensaje': mensaje,
            'error': error
        }

        mensaje = None
        error = False
        
        return render(request, 'carro.html', contexto)
    except:
        return render(request, 'carro.html')


def actualizar(request):
    data = {
        'id_libro': request.POST['id_libro'],
        'cantidad': request.POST['cantidad']
    }
    requests.put(
        'http://127.0.0.1:5000/biblioteca/carro/modificar/articulo', json=data)
    return redirect('carro')


def eliminarArticulo(request, id):
    global mensaje
    global error
    try:
        requests.delete(
            f'http://127.0.0.1:5000/biblioteca/articulo/eliminar/{id}')
        mensaje = 'El articulo se elimino correctamente'
        error = False
    except:
        mensaje = 'Error al eliminar el articulo'
        error = True

    return redirect('carro')

def realizarCompra(request):
    global mensaje
    global error
    try:
        requests.delete('http://127.0.0.1:5000/biblioteca/realizarCompra')
        mensaje = 'Compra realizada con exito'
        error = False
    except:
        mensaje = 'Error al realizar la compra'
        error = True

    return redirect('carro')

