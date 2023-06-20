from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from .models import Mascotas
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import MascotasForm,RegistroUserForm


def inicio(request):
    return render(request, 'Inicio.html')

def misionvision(request):
    return render(request, 'misionvision.html')

def porqueayudar(request):
    return render(request, 'porqueayudar.html')

def sobreperros(request):
    return render(request, 'sobreperros.html')

def otra(request):
     mascotas = Mascotas.objects.raw('select * from mascotas_mascotas')
     datos={
          'cositas':mascotas
     }
     return render(request, 'otra.html', datos)

@login_required
def crear(request):
     if request.method=="POST":    
          mascotasform = MascotasForm(request.POST,request.FILES)    #creamos un objeto de tipo Formulario
          if mascotasform.is_valid():
               mascotasform.save()      #similar al insert de sql en función 
               return redirect('inicio')
     else: 
         mascotasform=MascotasForm()
     return render(request, 'crear.html', {'Mascotas_form':mascotasform})


@login_required
def modificar(request, id):
     MascotasModificado=Mascotas.objects.get(patente=id)
     datos = {
          'form' : MascotasForm(instance=MascotasModificado)
     }

def registrar(request):
    data={
        'form':RegistroUserForm()
    }
    if request.method=="POST":
        formulario = RegistroUserForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], 
                    password=formulario.cleaned_data["password1"])
            login(request,user)
            return redirect ('inicio')
        data["form"] = formulario
    return render(request, 'registration/registrar.html',data)