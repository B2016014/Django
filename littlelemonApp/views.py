from django.shortcuts import render
from .models import menu
from .forms import BookingForm

# Create your views here.
def home(request):
    return render(request,'home.html')

def Menu(request):
    menus=menu.objects.all()
    return render(request,'menu.html',{'menu':menus})

def MenuItem(request,id):
    item=menu.objects.get(id=id)
    return render(request,'menu_item.html',{'item':item})

def about(request):
    return render(request,'about.html')

def book(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'book.html', {'form':form})

