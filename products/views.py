from django.shortcuts import render
from .models import Product


def all_products(request):
    """ Display all products with optional sorting, filtering by category and search functionality """
    products = Product.objects.all()
    
    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)