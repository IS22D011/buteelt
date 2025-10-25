from django.shortcuts import render, redirect, get_object_or_404
from app.models import Product
from .models import Cart, CartItem


# ✅ a. session key үүсгэх функц
def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart


# ✅ b. сагсанд бараа нэмэх
def add_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    cart_id = _cart_id(request)

    cart, created = Cart.objects.get_or_create(cart_id=cart_id)

    # CartItem шалгах
    try:
        cart_item = CartItem.objects.get(product=product, cart=cart)
        if cart_item.quantity < product.stock:  # барааны үлдэгдлээс хэтрэхгүй
            cart_item.quantity += 1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(
            product=product,
            quantity=1,
            cart=cart,
        )
        cart_item.save()

    return redirect('cart')


# ✅ c. тоо ширхэгийг 1-р бууруулах
def remove_cart(request, product_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    product = get_object_or_404(Product, id=product_id)
    cart_item = CartItem.objects.get(product=product, cart=cart)

    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart')


# ✅ d. тухайн барааг бүрэн устгах
def remove_cart_item(request, product_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    product = get_object_or_404(Product, id=product_id)
    cart_item = CartItem.objects.get(product=product, cart=cart)
    cart_item.delete()
    return redirect('cart')


# ✅ e. cart хуудас руу мэдээлэл дамжуулах
def cart(request, total=0, quantity=0, cart_items=None):
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart, is_active=True)
        for item in cart_items:
            total += (item.product.price * item.quantity)
            quantity += item.quantity
    except Cart.DoesNotExist:
        cart_items = []
    
    context = {
        'total': total,
        'quantity': quantity,
        'cart_items': cart_items,
    }
    return render(request, 'cart.html', context)
