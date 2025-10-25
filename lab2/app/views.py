from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from django.core.paginator import Paginator
from django.db import connection


def dict_fetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [dict(zip(columns, row)) for row in cursor.fetchall()]


def index(request):
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT b.product_name as product_name, b.price as price, b.images as images, 
                   d.category_name as category_name, b.slug as slug   
            FROM app_product b
            INNER JOIN app_category d ON b.category_id = d.id
            WHERE b.is_available = TRUE
            ORDER BY b.id DESC
            LIMIT 4
        """)
        products = dict_fetchall(cursor)

        cursor.execute("SELECT * FROM app_category")
        categories = dict_fetchall(cursor)

    return render(request, 'index.html', {
        'products': products,
        'categories': categories,
        'product_count': len(products)
    })


def store(request):
    products = Product.objects.filter(is_available=True)
    categories = Category.objects.all()

    paginator = Paginator(products, 6)  # Нэг хуудсанд 6 бүтээгдэхүүн
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'store.html', {
        'products': page_obj,
        'categories': categories,
        'product_count': products.count(),
        'page_obj': page_obj
    })


def show_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = Product.objects.filter(category=category, is_available=True)
    categories = Category.objects.all()

    paginator = Paginator(products, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'store.html', {
        'category': category,
        'products': page_obj,
        'categories': categories,
        'product_count': products.count(),
        'page_obj': page_obj
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


def place_order(request):
    return render(request, 'place_order.html')
