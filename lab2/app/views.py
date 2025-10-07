from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from django.db import connection

def index(request):
    with connection.cursor() as cursor:
        # Product хүснэгтээс 4 ширхэг идэвхтэй бүтээгдэхүүн
        cursor.execute("""
            SELECT b.product_name as product_name, b.price as price, b.images as images, d.category_name as category_name, b.slug as slug   
            FROM app_product b
            INNER JOIN app_category d ON b.category_id=d.id
            WHERE is_available = TRUE
            ORDER BY b.id DESC
            LIMIT 4
        """)
        products = dict_fetchall(cursor) #Cursor-аас авсан category-уудыг dictionary list болгон хадгална.
        # Category хүснэгтээс бүх category
        cursor.execute("SELECT * FROM app_category")
        categories = dict_fetchall(cursor)
        product_count = len(products)  # Python-д тоолж байна

    return render(request, 'index.html', {
        'products': products,
        'categories': categories,
        'product_count': product_count
    })
def dict_fetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]   #SQL query-ээр авсан үр дүнгийн баганын мэдээллийг агуулдаг.
    return [
        dict(zip(columns, row))  #Tuple-ийг dictionary болгож баганын нэр + утгыг хослуулна.
        for row in cursor.fetchall()
    ]

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

def show_category(request, slug):
    category = get_object_or_404(Category, slug = slug)
    product = Product.objects.filter(category = category, is_available =True)
    categories = Category.objects.all()
    context= {
        'category':category,
        'products': product,
        'categories': categories,
        'product_count': product.count()
    }
    return render(request, 'store.html', context)

