from django.shortcuts import render
from registro_clientes.models import cliente

def mostrar_inicio(request):
    return render(request, "registro_clientes/index.html")

def registrar_cliente(request):
    lista_cliente = cliente.objects.all()
    return render(request, "registro_clientes/clientes.html", 
                {"lista_cliente": lista_cliente})
