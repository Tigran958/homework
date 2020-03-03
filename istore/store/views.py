from django.shortcuts import render, get_object_or_404
# from django.views.generic import ListView
from .models import Product


# class ProductList(ListView):
#     model = Product

def home(request):
	prod_list = Product.objects.all()
	context = {"prod_list": prod_list} 
	return render(request,'store/product_list.html', context)


	

def detail(request,product_id):
	product = get_object_or_404(Product, pk=product_id)
	return render(request, 'store/detail.html', {"product": product})

def new_test(request,product_id):
	product = get_object_or_404(Product, pk=product_id)
	return render(request, 'store/new_test.html', {"product": product})