from django.urls import path, include
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', home, name="home"),

    #GENEROS
     path('generos/', GeneroList.as_view(), name="generos"),
    path('genero_create/', GeneroCreate.as_view(), name="genero_create"),
    path('genero_update/<int:pk>', GeneroUpdate.as_view(), name="genero_update"),
    path('genero_delete/<int:pk>', GeneroDelete.as_view(), name="genero_delete"),
   
    #LIBROS
  
    path('libros/', LibroList.as_view(), name="libros"),
    path('libro_create/', LibroCreate.as_view(), name="libro_create"),
    path('libro_update/<int:pk>', LibroUpdate.as_view(), name="libro_update"),
    path('libro_delete/<int:pk>', LibroDelete.as_view(), name="libro_delete"),
    
    #AUTORES
    path('autores/', AutorList.as_view(), name="autores"),
    path('autor_create/', AutorCreate.as_view(), name="autor_create"),
    path('autor_update/<int:pk>', AutorUpdate.as_view(), name="autor_update"),
    path('autor_delete/<int:pk>', AutorDelete.as_view(), name="autor_delete"),
   

     #BUSCADORES
     path('buscar/', buscar, name="buscar"),
     path('buscarLibros/', buscarLibros, name="buscarLibros"),
    
    #LOGIN, LOGOUT Y REGISTRO
    path('login/', login_request, name="login"),
    path('registro/', register, name="registro"),
    path('logout/', LogoutView.as_view(template_name="aplicacion/logout.html"), name="logout"),
    path('editarPerfil/', editarPerfil, name="editarPerfil"),
    path('agregarAvatar', agregarAvatar, name="agregarAvatar"),

    #ACERCA DE MI
    path('acercaDeMi/', acercaDeMi, name="acercaDeMi"),
]   