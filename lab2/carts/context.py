from .models import *
from .views import _cart_id
def cart_items(request):
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        items = CartItem.objects.filter(cart=cart, is_active=True)
        count = sum(item.quantity for item in items)
    except Cart.DoesNotExist:
        count = 0
    
    return {'cart_items_count': count}