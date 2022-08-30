from django.urls import path
from . import views

app_name = 'AppEntrega'

urlpatterns = [
    path('profesores/', views.profesores, name='profesores'),
    path('socios/', views.socios, name='socios'),
    path('deportes/', views.deportes, name='deportes'),
    
    path('', views.inicio, name='inicio'),
    path('form/profesor/', views.postProfesor, name='profeFormulario'),
    path('form/socio/', views.postSocio, name='socioFormulario'),
    path('form/deporte/', views.postDeporte, name='deporteFormulario'),
    path('deporte/', views.getDeporte, name='getDeporte'),
]