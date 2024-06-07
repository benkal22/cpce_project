#Models lib
from economic_exchanges.models.products import Product

from django.shortcuts import render, redirect, get_object_or_404


#View product / Secteur d'activité économique
def product_home(request):
    products = Product.objects.all()
    return render(request, 'economic_exchanges/product/product_list.html', {'products': products})

def product_detail(request, id):
    product = Product.objects.get(product_id=id)
    return render(request, 'economic_exchanges/product/product_detail.html', 
                  {'product_id':id, 'product': product})