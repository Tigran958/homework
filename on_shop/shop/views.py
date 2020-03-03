from django.shortcuts import render, get_object_or_404
from .models import Product, PType

# Create your views here.

def home(request):
	prod_l = Product.objects.all()
	prod_t = PType.objects.all()
	context = {"prod_l": prod_l, 'prod_t': prod_t}
	return render(request, 'shop/home.html', context)

def products(request,ptype_id):
	prod = get_object_or_404(PType, pk=ptype_id)
	prod_t = PType.objects.all()
	product = Product.objects.all().filter(ptype__p_type=prod.p_type)
	return render(request, 'shop/products.html', {"product": product, "prod_t": prod_t})

def details(request,product_id):
	detail = get_object_or_404(Product, pk=product_id)
	prod_t = PType.objects.all()
	return render(request, 'shop/details.html', {"detail": detail, "prod_t": prod_t})
