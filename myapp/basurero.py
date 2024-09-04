from typing import Any
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.db import models
from .models import Question,Choice,Imagen,Pregunta
from django.views  import generic
from .forms import CreateNewUser, CreateNewQuestion,Respuesta
from django.utils import timezone
from django.core.paginator import Paginator
 
from .forms import PreguntaForm
def mostrar_imagenes(request):

    imagenes = Imagen.objects.all()
    form = PreguntaForm()

    if request.method == 'POST':
        form = PreguntaForm(request.POST)
        if form.is_valid():
            pregunta = form.cleaned_data['pregunta']
         
            print(pregunta)
            return render(request, 'detail.html', {'imagenes': imagenes, 'form': form})
        





def gatitos(request):


    imagenes= Imagen.objects.all()
    forms= []
    for imagen in imagenes:
        preguntas= imagen.pregunta_set.all()
        form= Respuesta()
    
    if request.method== 'POST':
        form= Respuesta(request.POST)
        if form.is_valid():
            respuesta = form.save(commit=False)
            respuesta.imagen = imagen
            respuesta.save()

            pass
        else:
            form= Respuesta()
        
        forms.append({'imagen':imagen, 'form':form,'preguntas':preguntas})
        print (forms)

    return render(request, 'polls/gatitos.html',  {'forms':forms})