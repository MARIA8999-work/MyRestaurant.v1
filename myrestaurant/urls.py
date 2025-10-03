
from django.urls import path
from . import views


urlpatterns = [
    path('', views.Inicio, name='inicio'),
     path('Altas', views.altas, name='altas'),
]



