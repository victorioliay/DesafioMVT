from django.shortcuts import render
from MiApp.models import Familia

def mostrar_familia(request):

    familiar1 = Familia(nombre='Alley' , apellido='Liay' , edad=66 , fecha_de_nacimiento= '1966-11-21')
    familiar2 = Familia(nombre='Marisell' , apellido='Abbonizio' , edad=66 , fecha_de_nacimiento= '1967-01-20')
    familiar3 = Familia(nombre='Maria Paula' , apellido='Liay' , edad=30 , fecha_de_nacimiento= '1992-09-05')
    familiar4 = Familia(nombre='Maria Valentina' , apellido='Liay' , edad=27 , fecha_de_nacimiento= '1995-04-08')
# Create your views here.

    return render(request, 'MiApp/Templates/familia.html', {'familiares': [familiar1, familiar2, familiar3, familiar4]})