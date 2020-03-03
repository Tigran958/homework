from django.db import models

# Create your models here.
YEARS = [(x,x) for x in range(1940,2021)]

BODY_CHOICES = (
	(1, "sedan"),
	(2, "SUV"),
	(3, "Truck"),
)
class Car(models.Model):
	name = models.CharField(max_length=100)
	year = models.IntegerField(choices=YEARS)
	body = models.IntegerField(choices=BODY_CHOICES)

	def __str__(self):
		return self.name

class Part(models.Model):
	car = models.ForeignKey(Car,on_delete=models.CASCADE)
	name = models.CharField(max_length=200)
	price = models.IntegerField()
	
	def __str__(self):
		return self.name

