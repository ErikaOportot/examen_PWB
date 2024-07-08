from django.db import models

class Libro(models.Model):
    id_libro    = models.AutoField(db_column="idlibro", primary_key=True)
    titulo      = models.CharField(max_length=255, blank=False, null=False)
    anio        = models.IntegerField()
    descripcion_l = models.CharField(max_length=255, blank=False, null=False)

class Autor(models.Model):
    id_autor     = models.AutoField(db_column="idAutor", primary_key=True)
    nombre_autor = models.CharField(max_length=100, blank=False, null=False)
    nacionalidad = models.CharField(max_length=100, blank=False, null=False)
    

class Categoria(models.Model):
    id_categoria     = models.AutoField( db_column="idCategoria",primary_key=True)
    nombre_categoria = models.CharField(max_length=100)
    descripcion      = models.CharField(max_length=100)


class Navbar(models.Model):
    id_navbar = models.AutoField(db_column="idNavbar", primary_key=True)
    nombre = models.CharField(max_length=50)
    url = models.CharField(max_length=100)
