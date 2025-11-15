from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def bag_contents(request):
   
    bag_items = []
    total = Decimal('0.00')
    product_count = 0
    bag = request.session.get('bag', {})


    FREE_DELIVERY_THRESHOLD = Decimal(settings.FREE_DELIVERY_THRESHOLD)
    STANDARD_DELIVERY_PERCENTAGE = Decimal(settings.STANDARD_DELIVERY_PERCENTAGE)

    # Delivery logic
    if total < FREE_DELIVERY_THRESHOLD:
        delivery = total * (STANDARD_DELIVERY_PERCENTAGE / Decimal('100'))
        free_delivery_delta = FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = Decimal('0.00')
        free_delivery_delta = Decimal('0.00')

    grand_total = total + delivery

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context