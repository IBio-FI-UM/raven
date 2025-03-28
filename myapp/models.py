import datetime
from django.db import models
from django.utils import timezone



class Codigo(models.Model):
    codigo = models.CharField(max_length= 200)
    genero=models.CharField(max_length=200)
    facultad=models.CharField(max_length=200)
    def __str__(self):
        return self.codigo + self.genero + self.facultad

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)



   
    def __str__(self):
        return self.codigo
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    

class Imagen(models.Model):
    name = models.CharField(max_length=200)
    imagen= models.ImageField(upload_to='imagenes/')   
    #date = models.DateField("date published",null=True)
    #opcion=models.CharField(max_length=200,default='SOME STRING')
    def __str__(self):
        return self.name
    
class  Pregunta(models.Model):
    usuario_nombre= models.CharField(max_length=255, blank=True ,null=True)
    respuesta = models.IntegerField(choices=[(i, str(i)) for i in range(1, 9)])
    imagen= models.ForeignKey(Imagen, on_delete=models.CASCADE,null=True, blank=True)   
    #codigo= models.ForeignKey(Usuario, on_delete=models.CASCADE)
    def __str__(self):
        return  f"{self.usuario_nombre}: {self.respuesta}"



