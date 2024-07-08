from django.shortcuts import render
from .models import *



def index(request):
	Navbars = Navbar.objects.all()
	context = {
				"Navbars": Navbars,
			}
	return render (request, 'catalogo/index.html', context)

def libros(request):
	Navbars = Navbar.objects.all()
	Libros = Libro.objects.all()
	context = { "Navbars": Navbars,
              	"Libros": Libros}
	return render (request, 'catalogo/libros.html', context)

def autores(request):
	Navbars = Navbar.objects.all()
	Autores = Autor.objects.all()
	context = {"Navbars": Navbars,
            "Autores": Autores }
	return render (request, 'catalogo/Autores.html', context)

def categorias(request):
	Navbars = Navbar.objects.all()
	Categorias = Categoria.objects.all()
	context = { "Navbars": Navbars,
            "Categorias": Categorias }
	return render (request, 'catalogo/Categorias.html', context)