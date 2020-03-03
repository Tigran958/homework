from django.db import models


class Customer(models.Model):
	name = models.CharField(max_length = 100)
	last_name = models.CharField(max_length = 100)
	age = models.IntegerField()

	def __str__(self):
		return self.name

class Agreement(models.Model):
	name = models.ForeignKey(Customer, on_delete = models.CASCADE)
	number = models.IntegerField()
	amount = models.IntegerField()
	give_date = models.DateTimeField(auto_now_add = True)
	def __str__(self):
		self.a = "N " + str(self.number)
		return self.a

class Balance(models.Model):
	agrcode = models.ForeignKey(Agreement, on_delete = models.CASCADE)
	cust = models.ForeignKey(Customer, on_delete = models.CASCADE)
	account = models.CharField(max_length = 16)
	currency = models.CharField(max_length = 3)
	loans = models.IntegerField()

	def __str__(self):
		return str(self.agrcode.name)[0] + self.account

# Create your models here.
