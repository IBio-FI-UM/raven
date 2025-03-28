from typing import Any
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.db import models
from .models import Question,Choice,Imagen,Pregunta
from django.views  import generic
from .forms import CreateNewUser, CreateNewQuestion,Respuesta
from django.utils import timezone
from django.core.paginator import Paginator
 




#<li>
    #<a href="{% url 'myapp:reiniciar_encuesta' %}"> Reiniciar</a>

    #<li>
       # <a href="{% url 'myapp:pedir_usuario' %}"> Inicio</a>
       
    
   # </li>
#</li>

#path('pedir_usuario/encuesta/reiniciar/', views.encuesta, {'reiniciar': True}, name='reiniciar_encuesta'),


def encuesta(request,reiniciar=False):

    if reiniciar or 'imagen_actual' not in request.session:
        
        imagenes = Imagen.objects.all()
        if imagenes:
            request.session['imagen_actual'] = 1
        else:
    
            return render(request, 'index.html')

    imagen_actual_id = request.session['imagen_actual']
    imagen_actual = Imagen.objects.get(pk=imagen_actual_id)
    
    if request.method == 'POST':
        
        usuario_nombre = request.POST.get("usuario_nombre")
        respuesta_form = PreguntaForm(request.POST)  
        if respuesta_form.is_valid() and usuario_nombre:
            respuesta = respuesta_form.save(commit=False)
            respuesta.imagen = imagen_actual  
            respuesta.usuario_nombre = usuario_nombre  # Guardar el usuario sin necesidad de autenticación
            respuesta.save()
            
         
            siguiente_id = imagen_actual_id + 1
            siguiente_imagen = Imagen.objects.filter(pk=siguiente_id).first()
            if siguiente_imagen:
                request.session['imagen_actual'] = siguiente_id
                return redirect('.')
            else:
                return redirect ('reiniciar/')
    else:
        respuesta_form = PreguntaForm()
    
    return render(request, 'polls/encuesta.html', {'imagen': imagen_actual, 'respuesta_form': respuesta_form})












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