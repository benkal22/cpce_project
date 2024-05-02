from django.http import HttpResponse
from django.shortcuts import render

def producer_home(request):
    return HttpResponse('<h1>Mon espace de production</h1>')

def supplier_home(request):
    return HttpResponse('<h1>Mes fournisseurs</h1>')

def customer_home(request):
    return HttpResponse('<h1>Mes clients</h1>')
