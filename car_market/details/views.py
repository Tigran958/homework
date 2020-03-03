from django.shortcuts import render
from django.http import HttpResponse
from .models import Part, Car
# Create your views here.
def car_details(request):
	car_d = Part.objects.all()
	car1 = Car.objects.all()
	b = {}
	for i in car_d:

		if i.car.name not in b.keys():
			b[str(i.car.name)] = i.price
		else:
			b[str(i.car.name)] += i.price	

	# n_list.append(b)
	return HttpResponse(F'{b}')