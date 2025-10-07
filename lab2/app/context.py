from .models import *

def menu_links(request):
    category = Category.objects.all()
    return {'links':category}