# Generated by Django 4.1.2 on 2024-07-07 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id_autor', models.AutoField(db_column='idAutor', primary_key=True, serialize=False)),
                ('nombre_autor', models.CharField(max_length=100)),
                ('nacionalidad', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='categoria',
            fields=[
                ('id_categoria', models.AutoField(db_column='idCategoria', primary_key=True, serialize=False)),
                ('nombre_categoria', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id_libro', models.AutoField(db_column='idlibro', primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=255)),
                ('anio', models.IntegerField()),
                ('descripcion_l', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Navbar',
            fields=[
                ('id_navbar', models.AutoField(db_column='idNavbar', primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('url', models.CharField(max_length=100)),
            ],
        ),
    ]