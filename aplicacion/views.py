from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin # para clases
from django.contrib.auth.decorators import login_required # para funciones(se aplica con un arroba antes de la funcion ej @login)
from .forms import *
# Create your views here.
def home(request):
    return render(request, "aplicacion/home.html")

def acercaDeMi(request):
    return render(request, "aplicacion/acercaDeMi.html")

#GENEROS______________________________________________

class GeneroBaseView(LoginRequiredMixin):
    model = Genero
    fields = ['nombre','descripcion']
    success_url = reverse_lazy('generos')

class GeneroList(ListView):
    model = Genero

class GeneroCreate(GeneroBaseView,CreateView):
    pass

class GeneroUpdate(GeneroBaseView, UpdateView):
    pass

class GeneroDelete(GeneroBaseView, DeleteView):
    pass

#LIBROS______________________________________________

class LibroBaseView(LoginRequiredMixin):
    model = Libro
    fields = ['titulo','autor','año_publicacion','genero','sintaxis']
    success_url = reverse_lazy('libros')

class LibroList(ListView):
    model = Libro
#se pueden utilizar solo logueados
class LibroCreate(LibroBaseView, CreateView):
    pass

class LibroUpdate(LibroBaseView, UpdateView):
    pass

class LibroDelete(LibroBaseView, DeleteView):
    pass

#AUTORES______________________________________________

class AutorBaseView(LoginRequiredMixin):
    model = Autor
    fields = ['nombre', 'apellido', 'perfil', 'nacimiento']
    success_url = reverse_lazy('autores')

class AutorList(ListView):
    model = Autor

class AutorCreate(AutorBaseView, CreateView):
    pass

class AutorUpdate(AutorBaseView, UpdateView):
    pass

class AutorDelete(AutorBaseView, DeleteView):
    pass


 #BUSCADORES       
def buscar(request):
    return render(request, "aplicacion/buscar.html")

def buscarLibros(request):
    if 'buscar' in request.GET:
        patron = request.GET["buscar"]
        libros = Libro.objects.filter(genero__icontains=patron)
        contexto = {"libros": libros}
        return render(request, "aplicacion/libros.html", contexto)
    return HttpResponse("No se ingresaron patrones de búsqueda")

#LOGIN ,LOGOUT, REGISTRACION

def login_request(request):
    if request.method == "POST":
        usuario = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=usuario, password=password)

        if user is not None:
            login(request,user)

            #AVATAR
            try:
                avatar = Avatar.objects.get(user=request.user.id).imagen.url
            except:
                avatar = "/media/avatares/default.png"
            finally:
                request.session["avatar"] = avatar

            return render(request,'aplicacion/home.html')
        else:
            return redirect(reverse_lazy('login'))
       
    miForm = AuthenticationForm()

    return render(request, "aplicacion/login.html", {"form": miForm})

def register(request):
    if request.method == "POST":
        miForm = RegistroForm(request.POST)
        if miForm.is_valid():
            usuario = miForm.cleaned_data.get("username")
            miForm.save()
            return redirect(reverse_lazy('home'))

    else:    
        miForm = RegistroForm()

    return render(request, "aplicacion/registro.html", {"form": miForm }) 

#EDITAR PERFIL
@login_required
def editarPerfil(request):
    usuario = request.user

    if request.method == "POST":
        form = UserEditForm(request.POST)
        if form.is_valid():

            informacion = form.cleaned_data
            user = User.objects.get(username=usuario)
            user.email = informacion['email']
            user.first_name = informacion['first_name']
            user.last_name = informacion['last_name']
            user.set_password(informacion['password1'])
            user.save()
            return render(request,'aplicacion/home.html')
    else:
         form = UserEditForm(instance=usuario)
    
    return render(request, 'aplicacion/editarPerfil.html', {'form' :form})


@login_required
def agregarAvatar(request):
     if request.method == "POST":
        form = AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            usuario = User.objects.get(username = request.user)
            #Para borrar el avatar viejo
            avatarViejo = Avatar.objects.filter(user=usuario)
            if len(avatarViejo)>0:
                for i in range(len(avatarViejo)):
                    avatarViejo[i].delete()
            
            avatar = Avatar(user=usuario, imagen=form.cleaned_data['imagen'])
            avatar.save()

#Hago una url de la imagen en el request
            imagen = Avatar.objects.get(user=request.user.id).imagen.url
            request.session['avatar'] = imagen
            return render(request, "aplicacion/home.html")

     else:
          form = AvatarForm()

     return render(request, 'aplicacion/agregarAvatar.html', {'form' :form})


