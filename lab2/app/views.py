from django.shortcuts import render
from .models import Product, Category
from django.shortcuts import render, get_object_or_404


def index(request):
    products = Product.objects.filter(is_available=True)[:8]  # зөвхөн байгаа бараанаас эхний 8-г авна
    categories = Category.objects.all()
    return render(request, 'index.html', {
        'products': products,
        'categories': categories
    })

def cart(request):
    return render(request, 'cart.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def order_complete(request):
    return render(request, 'order_complete.html')

def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'product-detail.html', {'product': product})

def register(request):
    return render(request, 'register.html')

def search_result(request):
    return render(request, 'search-result.html')

def signin(request):
    return render(request, 'signin.html')

def store(request):
    return render(request, 'store.html')

def place_order(request):
    return render(request, 'place_order.html')

