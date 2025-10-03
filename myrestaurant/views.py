
from django.shortcuts import render, redirect
from django.db import connection

from .models import Platillo

def Inicio(request):

    return render(request, 'index.html')

#añadido por mi

def Altas(request):
    return render(request, 'altas.html')

""""
def index(request):
    return render(request, 'myrestaurant/index.html')



def eliminar(request):
    return render(request, 'myrestaurant/eliminar.html')

def modificar(request):
    return render(request, 'myrestaurant/modificar.html')

    s
        
    if request.method == "POST":
        platillo_id = request.POST.get('platillo_id')
        platillo = Platillo.objects.get(id=platillo_id)

        platillo.nombre = request.POST.get('nombre')
        platillo.descripcion = request.POST.get('descripcion')
        platillo.precio = request.POST.get('precio')
        platillo.categoria = request.POST.get('categoria')
        platillo.es_vegano = 'es_vegano' in request.POST
        platillo.contiene_alergenos = 'contiene_alergenos' in request.POST
        platillo.imagen_url = request.POST.get('imagen_url')

        platillo.save()
        return redirect('inicio')  # o 'tabla' según tu urls.py

    platillos = Platillo.objects.all()

    try:
        connection.ensure_connection()
        status = "Conexión exitosa a la base de datos"
    except Exception as e:
        status = f"Error de conexión: {e}"
"""