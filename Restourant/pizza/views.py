from django.shortcuts import render
from django.http import HttpResponse
from .models import Pizza, Topping

# Create your views here.

def getpizza(request):
	calculated_pizzas_list = []
	context_pizzas = Pizza.objects.filter(spicy = True)

	for i in context_pizzas:
		for j in i.toppings.all():
			i.price += j.price
		calculated_pizzas_list.append(i)
		print(i)
	return HttpResponse(calculated_pizzas_list)