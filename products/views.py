from django.shortcuts import render, get_object_or_404
from .models import Product
from django.db.models import Q
from .models import Product, Category

def all_products(request):
    products = Product.objects.all()
    query = None
    selected_categories = None
    current_category_display_name = None
    sort = request.GET.get('sort')
    direction = request.GET.get('direction', 'asc')

    # Category filtering
    category_param = request.GET.get('category')
    if category_param:
        selected_categories = category_param.split(',')
        products = products.filter(category__name__in=selected_categories)
        selected_categories_qs = Category.objects.filter(name__in=selected_categories)
        if selected_categories_qs.exists():
            current_category_display_name = selected_categories_qs.first().display_name

    # Search
    search_term = request.GET.get('q')
    if search_term:
        search_filter = Q(name__icontains=search_term) | Q(description__icontains=search_term)
        products = products.filter(search_filter)
        if not products.exists():
            messages.warning(request, "No products match your search.")
    elif 'q' in request.GET and not search_term:
        # Empty search query
        messages.error(request, "You didn't enter any search terms.")
        return redirect(reverse('products'))

    # Sorting
    if sort in ['name', 'price']:
        order_prefix = '' if direction == 'asc' else '-'
        products = products.order_by(f"{order_prefix}{sort}")

    context = {
        'products': products,
        'categories': Category.objects.all(),
        'current_categories': selected_categories,
        'current_category_display_name': current_category_display_name,
        'search_term': search_term,
        'sort': sort,
        'direction': direction,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ Display a single product's details"""
    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)