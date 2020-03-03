from django.db import models

class Person(models.Model):
	name = models.CharField(max_length = 200)
	surename = models.CharField(max_length = 200)

class Car(models.Model):
	question = models.ForeignKey(Person, on_delete = models.CASCADE)
	car = models.CharField(max_length = 200)
	car_year = models.DateTimeField(default = 0)