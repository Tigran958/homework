from django.db import models


THICKNESS_CHOICES = (
	(1, 'Americano'),
	(2, 'Italiano'),
)
# Create your models here.
class Topping(models.Model):
	name = models.CharField(max_length=100)
	price = models.IntegerField(default=0)

	def __str__(self):
		return self.name

class Pizza(models.Model):
	toppings = models.ManyToManyField(Topping)
	price = models.IntegerField(default=0)
	name = models.CharField(max_length=100)
	thickness = models.IntegerField(default=0)
	spicy = models.BooleanField(default=False) 

	
	def __str__(self):
		return self.name + " " + str(self.price)

