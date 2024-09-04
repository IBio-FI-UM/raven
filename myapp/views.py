from typing import Any
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.db import models
from .models import Imagen,Pregunta
from django.views  import generic
from .forms import CreateNewUser, CreateNewQuestion, UsuarioForm
from django.utils import timezone
from django.core.paginator import Paginator

class indexVIew(generic.ListView):
    template_name = "polls/detail.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published questions."""
        return Imagen.objects.order_by('id')[:5] 


def intro(request):
    if request.method == 'POST':
        user= UsuarioForm(request.POST)
        if user.is_valid():
            post= user.save()
            post.save()
            return redirect('detail/')
    else:
        user= UsuarioForm()
    context = {
        'user': user,

    }
    return render(request, 'polls/usuario.html', context)
def Detalle(request):
    return render(request,'polls/detail.html')
def gatitos(request):
    return render(request, 'polls/gatitos.html')    
from django.core.paginator import Paginator
from .forms import PreguntaForm
from django.shortcuts import render, redirect
from .models import Imagen
from .forms import PreguntaForm

from django.shortcuts import render, redirect
from .models import Imagen
from .forms import PreguntaForm  

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
        respuesta_form = PreguntaForm(request.POST)  
        if respuesta_form.is_valid():
            respuesta = respuesta_form.save(commit=False)
            respuesta.imagen = imagen_actual  
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



def mostrada_imagen(request):
    

    imagen_no_respondida = Imagen.objects.filter(pregunta__isnull=True).first()
    if imagen_no_respondida:
        form = PreguntaForm(instance=imagen_no_respondida)
        if request.method == 'POST':
            pregunta= PreguntaForm(request.POST)
            if pregunta.is_valid():
                post= pregunta.save()
                post.save()
                return redirect('.')
        else:
            post= PreguntaForm(instance= imagen_no_respondida)
        
    context= {'imagen':imagen_no_respondida, 'post': post}

    return render(request, 'polls/encuesta.html', context)
 


def guardar_respuesta(request):

    respuesta_usuario = request.POST['pregunta']
    imagen_id = request.POST['imagen_id']

    imagen = Imagen.objects.get(pk=imagen_id)

    respuesta = Pregunta(imagen=imagen, respuesta=respuesta_usuario)
    respuesta.save()

    return redirect('mostrada_imagen')

def mostrar_imagenes(request):
    imagenes = Imagen.objects.all()  
    paginator= Paginator(imagenes,1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    #current_page = paginator.page(page)  # Get the current page
    if request.method == 'POST':
        pregunta_form = PreguntaForm(request.POST)
        if pregunta_form.is_valid():
            post= pregunta_form.save()
            post.save()





            #imagen_id = request.POST.get('imagen_id')
            #pregunta_texto = pregunta_form.cleaned_data['pregunta']  #de form es pregunta
            #imagen = Imagen.objects.get(id=imagen_id)
            #pregunta = Pregunta(imagen=imagen, pregunta=pregunta_texto)
            #pregunta.save()
            #return redirect('lista_imagenes')
    else:
        pregunta_form= PreguntaForm()
        #pregunta=Pregunta()
    context = {
        'imagenes': page_obj, 
        'pregunta_form': pregunta_form,
        

         # Use current_page.object_list
        #'paginator': paginator,
        #'page_number': current_page.number,  # Add page_number to context
    }
    return render(request, 'polls/detail.html', context)


def create_user(request):
    user= "rodrox"
    if request.method =='GET':
         return render(request, 'polls/create_user.html' , {'form': CreateNewUser()})

    else:
    
        return redirect( 'myapp:gatitos')
   

def create_question(request):
    if request.method== 'GET':
        return render(request, 'polls/create_question.html', {'form': CreateNewQuestion()})
    else:
        
        return  render(request, 'polls/create_question.html', {'form': CreateNewQuestion()})