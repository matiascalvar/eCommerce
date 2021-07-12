from django.urls import path, include
from . import views

app_name = "USUARIOS"
urlpatterns = [
    path('registrarse', views.registrarse, name="registrarse"),
    path('login', views.loginuser, name="login"),
    path('logout', views.logoutuser, name="logout"),
]