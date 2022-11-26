from django.shortcuts import render

def mostrar_inicio(request):
    return render(request, "registro_clientes/index.html")
