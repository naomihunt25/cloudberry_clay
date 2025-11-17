from decimal import Decimal
from django.conf import settings
from products.models import Product


def bag_contents(request):
    bag_items = []
    total = Decimal('0.00')
    product_count = 0
    bag = request.session.get('bag', {})

    for item_id, quantity in bag.items():
        try:
            product = Product.objects.get(pk=item_id)
        except (Product.DoesNotExist, ValueError, TypeError):
            continue
        try:
            item_total = quantity * product.price
        except Exception:
            item_total = Decimal('0.00')

        total += item_total
        product_count += quantity
        bag_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
            'subtotal': item_total,
        })

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
