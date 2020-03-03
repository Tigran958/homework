from django.urls import path 
from . import views

urlpatterns = [
	path('part', views.car_details),
]