from django.shortcuts import render
from django.http import HttpResponse
from .models import Customer, Agreement, Balance
# Create your views here.

def message(request):
	a = Customer.objects.all()[1]
	return HttpResponse(a.name + " " + a.last_name)

def new_message(request):
	b = Customer.objects.get(name = "Armen")
	print(b.)
	return HttpResponse(F"{b.name} {b.last_name}'s age is {b.age}. He has ")