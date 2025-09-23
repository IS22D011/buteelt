from django.shortcuts import render, get_object_or_404
from .models import Product, Category

def index(request):
    with connection.cursor() as cursor:
        # Product хүснэгтээс 4 ширхэг идэвхтэй бүтээгдэхүүн
        cursor.execute("""
            SELECT * FROM app_product
            WHERE is_available = TRUE
            LIMIT 4
        """)
        products = dict_fetchall(cursor)

        # Category хүснэгтээс бүх category
        cursor.execute("SELECT * FROM app_category")
        categories = dict_fetchall(cursor)

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

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'product-detail.html', {'product': product})

def register(request):
    return render(request, 'register.html')

def search_result(request):
    return render(request, 'search-result.html')

def signin(request):
    return render(request, 'signin.html')

def store(request):
    products = Product.objects.filter(is_available=True)  
    categories = Category.objects.all()
    product_count = products.count() 
    return render(request, 'store.html', {
        'products': products,
        'categories': categories,
        'product_count': product_count
    })

def place_order(request):
    return render(request, 'place_order.html')
