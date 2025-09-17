from django.contrib import admin
from django.urls import path
from app import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/',                    admin.site.urls),
    path("",                          views.index,          name='index'),
    path("cart",                      views.cart,           name='cart'),
    path("dashboard",                 views.dashboard,      name='dashboard'),
    path("order_complete",            views.order_complete, name='order_complete'),
    path("place_order",               views.place_order,    name='place_order'),
    path("product_detail",            views.product_detail, name='product_detail'),
    path("register",                  views.register,       name='register'),
    path("search_result",             views.search_result,  name='search_result'),
    path("signin",                    views.signin,         name='signin'),
    path("store",                     views.store,          name='store'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
