from USUARIOS.decorators import unauthenticated_user
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

@unauthenticated_user
def registrarse(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            usercreated = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for '+ usercreated)          
            return HttpResponseRedirect(reverse('login'))
    else:
        form = RegistroForm()
    return render(request, 'registration/registro.html', {
        'form': form
        })

@unauthenticated_user
def loginuser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Username or password is incorrect')
            
    return render(request, 'registration/login.html')

       
def logoutuser(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('index'))
    else:

        logout(request)
        return redirect('login')