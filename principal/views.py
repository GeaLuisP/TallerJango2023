from django.shortcuts import render

def inicio(request):
    titulo = "Inicio"
    nombre = "Luis Carlos Latorre Berdugo"
    context={
        "titulo": titulo,
        "nombre": nombre,
    }
    return render(request, 'index.html', context)