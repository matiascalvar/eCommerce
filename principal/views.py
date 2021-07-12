from django import forms
from django.forms import fields
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
# Create your views here.

#renderiza el index. 
def index(request):
    return render(request, "main/index.html",{
        "lista_productos": Product.objects.all()   
    })

def acercade(request):
    return render(request, "main/acercade.html")


#renderiza la pagina llamada product/.html y pasa por context un modelo dentro de una variable

def productos(request):
	products = Product.objects.all()
	return render(request, 'main/product.html', {'products':products})

class FormProductCustom(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

@login_required(login_url='login')
def producto_alta(request):
    form = FormProductCustom
    if request.method == "POST":
        form = FormProductCustom(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')


    context = {'form':form}
    return render(request, "main/producto_alta.html", context)

def customer(request, pk_test):
	customer = Customer.objects.get(id=pk_test)

	orders = customer.order_set.all()
	order_count = orders.count()

	context = {'customer':customer, 'orders':orders, 'order_count':order_count}
	return render(request, 'main/customer.html',context)