from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "Your bag is empty, please add something before checking out.")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51SU3NE7oUblbUovpmqlhjYw27YQGRmbFhxnIYFZRjbEBQ19I0B0ieBGVOMOBrDbfLkoUGAAJ7ahaTUElmksTs8nC00GFXycZls',
        'client_secret': 'test',
    }

    return render(request, template, context)