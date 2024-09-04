from django import forms
from .models import Pregunta, Codigo, Imagen


class CreateNewUser(forms.Form):
    title = forms.CharField(label="titulo",max_length= 200)
    description=forms.CharField(label="descripción", widget=forms.Textarea)

class CreateNewQuestion(forms.ModelForm):
    name= forms.CharField(label="Nombre de la pregunta", max_length=200)

class PreguntaForm(forms.ModelForm):
    class Meta:
        model= Pregunta
        fields =["respuesta"]
        exclude = ["imagen"]
        #fields = '__all__'



class UsuarioForm(forms.ModelForm):
    codigo = forms.CharField(label='codigo', widget=forms.Textarea(attrs={'rows':2,'placeholder':'Elija la opción'}),required=True)
    genero=forms.CharField(label='genero', widget=forms.Textarea(attrs={'rows':2,'placeholder':'Elija la opción'}),required=True)
    facultad=forms.CharField(label='facultad', widget=forms.Textarea(attrs={'rows':2,'placeholder':'Elija la opción'}),required=True)
    class Meta:
        model= Codigo
        fields = '__all__'

