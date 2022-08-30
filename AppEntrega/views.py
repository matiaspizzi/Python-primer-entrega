from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Deportes, Profesores, Socios
from AppEntrega.forms import formDeporte, formProfesor, formSocio

# Create your views here.


def inicio(request):
    return render(request, "Appentrega/inicio.html")


def profesores(request):
    profesores = Profesores.objects.all()
    return render(request, "Appentrega/profesores.html", {"profesores": profesores})


def socios(request):
    socios = Socios.objects.all()
    return render(request, "Appentrega/socios.html", {"socios": socios})

def deportes(request):
    deportes = Deportes.objects.all()
    return render(request, "Appentrega/deportes.html", {"deportes": deportes})


def getDeporte(request):
    if request.GET["deporte"]:
        depor = request.GET["deporte"]
        deporte = Deportes.objects.filter(nombre = depor)
        if len(deporte) != 0:
            return render(request, "Appentrega/deportes.html", {"deportes": deporte})
        else:
            return render(request, "Appentrega/deportes.html", {"mensaje": "No se encontraron deportes"})
    else:
        return redirect("AppEntrega:deportes")


def postDeporte(request):
    if request.method == "POST":
        form = formDeporte(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            nombre = info["nombre"]
            turno = info["turno"]
            comision = info["comision"]
            deporte = Deportes(nombre=nombre, turno=turno, comision=comision)
            deporte.save()
            return redirect("AppEntrega:deportes")
        else:
            return render(request, "Appentrega/deportes.html", {"mensaje": "Error"})
    else:
        form = formDeporte()
    return render(request, "Appentrega/deportes.html", {"formulario": form})



def postProfesor(request):
    if request.method == "POST":
        form = formProfesor(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            nombre = info["nombre"]
            apellido = info["apellido"]
            email = info["email"]
            profesion = info["profesion"]
            profesor = Profesores(nombre=nombre, apellido=apellido, email=email, profesion=profesion)
            profesor.save()
            return redirect("AppEntrega:profesores")
        else:
            return render(request, "Appentrega/inicio.html", {"mensaje": "Error"})
    else:
        form = formProfesor()
    return render(request, "Appentrega/formularioProfe.html", {"formulario": form})


def postSocio(request):
    if request.method == "POST":
        form = formSocio(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            nombre = info["nombre"]
            apellido = info["apellido"]
            dni = info["dni"]
            email = info["email"]
            socio = Socios(nombre=nombre, apellido=apellido, dni=dni, email=email)
            socio.save()
            return redirect("AppEntrega:socios")
        else:
            return render(request, "Appentrega/socios.html", {"mensaje": "Error"})
    else:
        form = formSocio()
    return render(request, "Appentrega/formularioSocio.html", {"formulario": form})


