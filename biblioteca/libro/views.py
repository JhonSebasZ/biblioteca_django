from django.shortcuts import render, redirect
import requests

mensaje = None

# Create your views here.
def crearLibro(request):
    if request.method == 'GET':
        return render(request, 'crearLibro.html')
    data = {
        'titulo': request.POST['titulo'].strip(),
        'autor': request.POST['autor'].strip(),
        'palabras_claves': request.POST['palabrasClaves'].strip().split(','),
        'categoria': request.POST['categoria'].strip(),
        'valor': int(request.POST['valor'].strip()),
        'imagen': request.POST['urlImagen'].strip(),
        'descripcion': request.POST['descripcion'].strip()
    }
    res = requests.post(
        'http://127.0.0.1:5000/biblioteca/libros', json=data).json()
    return render(request, 'crearLibro.html')


def libros(request):
    global mensaje
    try:
        respuesta = requests.get('http://127.0.0.1:5000/biblioteca/libros')
        libros = respuesta.json()
        contexto = {
            'libros': libros['data'],
            'mensaje': mensaje
        }
        mensaje = None
        return render(request, 'libros.html', contexto)
    except Exception as ex:
        print(ex)
        return render(request, 'libros.html')


def busacarLibros(request):
    categoria = request.POST['categoria']
    parametro = request.POST['parametro'].strip()
    respuesta = requests.get(
        f'http://127.0.0.1:5000/biblioteca/libros/{categoria}/{parametro}')
    libros = respuesta.json()
    # print('buscar libro', credenciales)
    return render(request, 'libros.html', {'libros': libros['data']})


def descripcionLibro(request, id):
    try:
        respuesta = requests.get(
            f'http://127.0.0.1:5000/biblioteca/libros/id_libro/{id}')
        libro = respuesta.json()

        return render(request, 'descripcionLibro.html', {'libro': libro['data'][0]})
    except:
        return render(request, 'descripcionLibro.html')


def agregarCarro(request, id):
    global mensaje
    data = {
        'id_libro': id,
        'cantidad': 1
    }
    requests.post('http://127.0.0.1:5000/biblioteca/agregarCarro', json=data)
    mensaje = 'El libro se agrego al carro de compras'
    return redirect('libros')


def agregarResena(request, id):
    if request.method == 'GET':
        return render(request, 'resena.html')
    data = {
        'comentario': request.POST['comentario'].strip(),
        'calificacion': request.POST['calificacion'],
        'id_libro': id
    }

    requests.post('http://127.0.0.1:5000/biblioteca/resenas', json=data)
    return redirect('descripcionLibro', id)


def listaDeseos(request):
    try:
        libros = requests.get(
            'http://127.0.0.1:5000//biblioteca/libros/deseos').json()

        return render(request, 'deseos.html', {'libros': libros['data']})
    except:
        return render(request, 'deseos.html')


def agregarDeseos(request, id):
    global mensaje
    requests.post(f'http://127.0.0.1:5000/biblioteca/agregar/deseos/{id}')
    mensaje = 'El libro se agrego a la lista de deseos'
    return redirect('libros')


def quitarLibroDeseo(request, id):
    res = requests.delete(
        f'http://127.0.0.1:5000/biblioteca/libros/deseos/eliminar/{id}').json()
    return redirect('listaDeseos')
