from django.urls import path
from . import views 

# Create your views here.
app_name= "myapp"
urlpatterns= [
path ("",views.indexVIew.as_view(),name="index"),
path("usuario/",views.intro,name="intro"),

path("encuesta/",views.encuesta,name="encuesta"),
path('encuesta/reiniciar/', views.encuesta, {'reiniciar': True}, name='reiniciar_encuesta'),
path("create_question/",views.create_question,name="create_question"),
path("create_user/",views.create_user,name="create_user"),
path("perritos/detail/",views.mostrar_imagenes, name="detail"),
]
