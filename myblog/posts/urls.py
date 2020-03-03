from django.urls import path
from . import views

urlpatterns = [
	path('1', views.first_post),
	path('2', views.second_post),
]