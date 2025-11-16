from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from .models import Product, Category
from .forms import ProductForm


def all_products(request):
    """ View all products with sorting, searching, and category filtering """
    products = Product.objects.all()

    selected_categories = None
    current_category_display_name = None
    search_term = None

    # Sorting
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
        queries = Q(name__icontains=search_term) | Q(description__icontains=search_term)
        products = products.filter(queries)

        if not products.exists():
            messages.warning(request, "No products match your search.")
    elif 'q' in request.GET and not search_term:
        messages.error(request, "You didn’t enter any search terms.")
        return redirect(reverse('products'))

    # Sorting logic
    if sort in ['name', 'price']:
        order_prefix = '' if direction == 'asc' else '-'
        products = products.order_by(f'{order_prefix}{sort}')

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
    product = get_object_or_404(Product, pk=product_id)

    return render(request, 'products/product_detail.html', {'product': product})


@login_required
def add_product(request):
    if not request.user.is_superuser:
        messages.error(request, "Only store owners can add products.")
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, f"Added '{product.name}' successfully!")
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, "Failed to add product. Please check the form.")
    else:
        form = ProductForm()

    return render(request, 'products/add_product.html', {'form': form})


@login_required
def edit_product(request, product_id):
    if not request.user.is_superuser:
        messages.error(request, "Only store owners can edit products.")
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, f"Updated '{product.name}' successfully!")
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, "Failed to update product. Please check the form.")
    else:
        form = ProductForm(instance=product)
        messages.info(request, f"You are editing '{product.name}'")

    return render(request, 'products/edit_product.html', {'form': form, 'product': product})


@login_required
def delete_product(request, product_id):
    if not request.user.is_superuser:
        messages.error(request, "Only store owners can delete products.")
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, f"'{product.name}' has been deleted.")

    return redirect(reverse('products'))
