from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages

from products.models import Product


def view_bag(request):
    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity', 1))
    redirect_url = request.POST.get('redirect_url', reverse('products'))
    bag = request.session.get('bag', {})

    if str(item_id) in bag:
        bag[str(item_id)] += quantity
        messages.info(request, f"Updated quantity for '{product.name}' in your bag.")
    else:
        bag[str(item_id)] = quantity
        messages.success(request, f"Added '{product.name}' to your bag.")

    request.session['bag'] = bag
    return redirect(redirect_url)


def update_bag(request, item_id):
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity', 1))
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[str(item_id)] = quantity
        messages.success(request, f"Updated '{product.name}' quantity to {quantity}.")
    else:
        bag.pop(str(item_id), None)
        messages.warning(request, f"Removed '{product.name}' from your bag.")

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    product = get_object_or_404(Product, pk=item_id)
    bag = request.session.get('bag', {})

    if str(item_id) in bag:
        bag.pop(str(item_id))
        messages.warning(request, f"Removed '{product.name}' from your bag.")
        request.session['bag'] = bag
    else:
        messages.error(request, f"'{product.name}' was not found in your bag.")

    return redirect(reverse('view_bag'))
