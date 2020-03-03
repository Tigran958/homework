from django.db import models

# Create your models here.

class Product(models.Model):
	product_name = models.CharField(max_length=50)
	description = models.TextField()
	price = models.IntegerField(default=0)
	location = models.CharField(max_length=100)
	image = models.ImageField(upload_to='images/')

	def __str__(self):
		return self.product_name