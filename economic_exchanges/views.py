from django.http import HttpResponse
from django.shortcuts import render
from .models import *

def product_home(request):
    products = Product.objects.all()
    return render(request, 'economic_exchanges/product.html', {'products': products})

def producer_home(request):
    producers = Producer.objects.all()
    return render(request, 'economic_exchanges/producer.html', {'producers': producers})


def supplier_home(request):
    return HttpResponse('<h1>Mes fournisseurs</h1>')

def customer_home(request):
    return HttpResponse('<h1>Mes clients</h1>')
