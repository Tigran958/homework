from django.urls import path 
from . import views

urlpatterns = [
	path('1', views.message),
	path('2', views.new_message),
]