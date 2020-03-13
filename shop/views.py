from django.shortcuts import render
from products.models import Product

# Create your views here.
def shop(request):
    products = Product.objects.all()
    return render(request, "shop.html", {"products": products})


def all_products(request):
    products = Product.objects.all()
    return render(request, "shop.html", {"products": products})


def get_product(request, id):
    product = Product.objects.get(id=id)
    return render(request, "product_detail.html", {"product": product})