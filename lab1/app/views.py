from django.shortcuts import render, redirect
from .models import Baraa
from .forms import BaraaForm
def index(request):
    baraa_list = Baraa.objects.all()

    if request.method == "POST":
        form = BaraaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = BaraaForm()

    return render(request, 'index.html', {'form': form, 'baraa_list': baraa_list})

