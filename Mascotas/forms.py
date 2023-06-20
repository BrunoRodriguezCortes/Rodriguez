from django import forms
from .models import Mascotas
from django.contrib.auth.forms import UserCreationForm
from django.forms.models import ModelChoiceField
from django.forms import widgets
from django.contrib.auth.models import User
from django.forms import ModelForm

class RegistroUserForm(UserCreationForm):
    class Meta:
        model= User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1']

class MascotasForm(forms.ModelForm):
    class Meta: 
        model = Mascotas
        fields = [ 'articulo', 'marca', 'imagen']
        labels = {
            'articulo': 'articulo',
            'marca' : 'Marca',
            'imagen':'Imagen'
        }
        widgets ={
            'articulo': forms.TextInput(
                attrs={
                    'placeholder':'Ingrese articulo..',
                    'id': 'articulo',
                    'class': 'form-control'
                }
            ),
            'marca': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese marca..',
                    'id': 'marca',
                    'class': 'form-control'
                }
            ),
            'imagen': forms.FileInput(
                attrs={
                    'id': 'imagen',
                    'class': 'form-control'
                }
            ),
           
        }