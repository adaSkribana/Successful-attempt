from django.shortcuts import render


def acerca(request):
    return render(request, "acerca/acerca.html")
