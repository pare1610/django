from django.shortcuts import render
from django.http import HttpResponse
from gestion_pedidos.models import Articulos


# Create your views here.
def busqueda_productos(request):
    return render(request, 'busqueda_productos.html')

def buscar(request):
    #return render(request, 'buscar.html')
    if request.GET["producto"]:    
        # mensaje=f"Articulo buscado: {request.GET['producto']}" 
        prd=request.GET['producto']
        articulo=Articulos.objects.filter(nombre__icontains=prd) 
        return render(request, 'resultados_busqueda.html',{"articulo":articulo,"query":prd})
    else:
        mensaje="No se ha introcido ningun valor"
    return HttpResponse(mensaje)

