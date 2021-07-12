from django.db import models

# Create your models here.
# Los modelos se pasan mediante una funcion en views que renderiza una página de templates
# los modelos se importan en views para poder ser utilizados posteriormente
# Deben ser registrados en admin.py

class Customer(models.Model):
	name = models.CharField(max_length=200, null=True)
	phone = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)


	def __str__(self):
		return self.name

##################################################

class Category(models.Model):
    name = models.CharField(max_length=64, null=True)
    descripcion = models.TextField(null=True)

    def __str__(self):
        return self.name

##################################################


class Product(models.Model):
    titulo = models.CharField(max_length=64, null=True)
    #imagen = models.ImageField(null=True)
    descripcion = models.TextField(null=True)
    precio = models.FloatField(null=True)
    categoria = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="categoria")
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.titulo

############# ################################## #########################

class Order(models.Model):
	STATUS = (
			('Pending', 'Pending'),
			('Out for delivery', 'Out for delivery'),
			('Delivered', 'Delivered'),
			)

	customer = models.ForeignKey(Customer, null=True, on_delete= models.SET_NULL)
	product = models.ForeignKey(Product, null=True, on_delete= models.SET_NULL)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	status = models.CharField(max_length=200, null=True, choices=STATUS)

