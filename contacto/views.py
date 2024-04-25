# En contact/views.py
from django.shortcuts import render, redirect
from .forms import ContactoForm
from .models import ContactoMessage


def contacto(request):
    if request.method == "POST":
        form = ContactoForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            mensaje = form.cleaned_data["message"]

            nuevo_mensaje = ContactoMessage(nombre=nombre, email=email, mensaje=mensaje)
            nuevo_mensaje.save()

            # return redirect("exito")
            return render(request, "contacto/exito.html")
    else:
        form = ContactoForm()
    return render(request, "contacto/contacto.html", {"form": form})


def exito(request):
    return render(request, "contacto/exito.html")
