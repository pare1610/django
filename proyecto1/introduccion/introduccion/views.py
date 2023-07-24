
from django.template import Template, Context, loader
from django.template.loader import get_template
from django.http import HttpResponse
from django.shortcuts import render

class Persona:
    def __init__(self, nombre, apellido):
        self.nombre=nombre
        self.apellido=apellido

def saludo(request):
    p1=Persona("Pedro", "Arévalo")
    temas_del_curso=["Plantillas", "Modelos", "Formularios", "Vistas", "Despliegue", "Bootstrap"]
   
    # doc_externo=get_template("inicio.html")
    # documento=doc_externo.render({"nombre":p1.nombre,"apellido":p1.apellido,"temas":temas_del_curso})

    return render(request, "inicio.html", {"nombre":p1.nombre,"apellido":p1.apellido,"temas":temas_del_curso})

def base(request):
    return render(request, "base.html")

def hija1(request):
    return render(request, "hija1.html")

def hija2(request):
    return render(request, "hija2.html")