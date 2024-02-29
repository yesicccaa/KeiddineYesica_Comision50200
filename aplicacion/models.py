from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Genero(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()

    def __str__(self):
        return f"{self.nombre}"

class Autor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    perfil = models.TextField()
    nacimiento = models.DateField()

    class Meta:
        verbose_name = "Autor"
        verbose_name_plural = "Autores"
        ordering = ["apellido", "nombre"]

    def __str__(self):
        return f"{self.nombre}, {self.apellido}"

class Libro(models.Model):
    titulo = models.CharField(max_length=50)
    autor = models.CharField(max_length=80)
    sintaxis = models.TextField()
    genero = models.CharField(max_length=50)
    año_publicacion = models.IntegerField()

    def __str__(self):
        return f"{self.titulo} - {self.autor}"
    
class Avatar(models.Model):
    imagen = models.ImageField(upload_to="avatares")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} - {self.imagen}"

    
