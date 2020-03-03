from django.urls import path

# from .views import ProductList
from . import views


urlpatterns = [
	# path('', ProductList.as_view(), name='home'),
    path('', views.home, name='home'),
	path('<int:product_id>/', views.detail, name='detail'),    
	path('<int:product_id>/test', views.new_test, name='new_test'),    
]