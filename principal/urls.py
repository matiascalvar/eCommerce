from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    #path('index', views.index, name="index"),
    path('product', views.productos, name="product"),
    path('acercade', views.acercade, name="acercade"),
    path('producto_alta', views.producto_alta, name="producto_alta"),
    path('customer/<str:pk_test>/', views.customer, name="customer"),

]
    #path('nombre_nella_url', views.nombre_della_funcion, name="no se aun")
"""
crear html dentro de templates/main
agregar path en urls de la app. Ya que al proyecto nuclear ya esta patheada la app
crear en VIEWS la funcion que renderiza el html

"""