from django.urls import path
from . import views

urlpatterns = [
	path("", views.home, name='home'),
	path("<int:ptype_id>/", views.products, name='new'),
	path("<int:product_id>/d", views.details, name='details'),
]