from django.shortcuts import render
from .models import *



def index(request):
			Libros = Libro.objects.all()  # <- agregamos esta linea
			context = { "Libros": Libros }
			return render (request, 'catalogo/index.html', context)

def libros(request):
			Libros = Libro.objects.all()  # <- agregamos esta linea
			context = { "Libros": Libros }
			return render (request, 'catalogo/libros.html', context)

def autores(request):
			Autores = Autor.objects.all()  # <- agregamos esta linea
			context = { "Autores": Autores }
			return render (request, 'catalogo/Autores.html', context)

def categorias(request):
			Categorias = Categoria.objects.all()  # <- agregamos esta linea
			context = { "Categorias": Categorias }
			return render (request, 'catalogo/Categorias.html', context)