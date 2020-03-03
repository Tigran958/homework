from django.db import models

# Create your models here.

class PType(models.Model):
	p_type = models.CharField(max_length=100)

	def __str__(self):
		return self.p_type


class Product(models.Model):
	ptype = models.ForeignKey(PType, on_delete=models.CASCADE)
	name = models.CharField(max_length=100)
	description = models.TextField()
	price = models.IntegerField(default=0)
	location = models.CharField(max_length=100)
	picture = models.ImageField(upload_to='images/')

	def __str__(self):
		return self.name
