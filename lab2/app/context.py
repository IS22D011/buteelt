from .models import *

def menu_links(request):
    category = Category.objects.all()
    return {'links':category}

def cart_items(request):
    return {'cart_items': request.session.get('cart', [])}
