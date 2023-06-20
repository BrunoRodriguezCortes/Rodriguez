from django.urls import path
from .views import inicio,misionvision,porqueayudar,sobreperros,registrar,modificar,otra,crear

urlpatterns=[ 
    path('', inicio, name="inicio"),
    path('misionvision/',misionvision, name="misionvision"), 
    path('porqueayudar/', porqueayudar, name="porqueayudar"),
    path('sobreperros/', sobreperros, name="sobreperros"),
    path('registrar/' , registrar, name="registrar"),
    path('modificar/<id>', modificar, name="modificar"),
    path('otra/', otra, name="otra"),
    path('crear/', crear, name="crear"),
   
]