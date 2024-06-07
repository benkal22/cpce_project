#Http lib
from django.http import HttpResponse
from django.http import JsonResponse

#Models lib
from economic_exchanges.models.producers import Producer
from economic_exchanges.models.products import Product
from economic_exchanges.models.suppliers import Supplier
from economic_exchanges.models.company_clients import CompanyClient
from economic_exchanges.models.personal_clients import PersonalClient
from economic_exchanges.models.purchases import Purchase
from economic_exchanges.models.sales import Sale

from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

#View Declaration achat et vente
def declaration_home(request):
    purchases = Purchase.objects.all()
    sales = Sale.objects.all()
    return render(request, 'economic_exchanges/declaration/declaration_list.html', {'purchases': purchases, 'sales': sales})

def declaration_purchase_detail(request, id):
    purchase = Purchase.objects.get(purchase_id=id)
    return render(request, 'economic_exchanges/declaration/declaration_purchase_detail.html', 
                  {'purchase_id':id, 'purchase': purchase})

def declaration_sale_detail(request, id):
    sale = Sale.objects.get(sale_id=id)
    return render(request, 'economic_exchanges/declaration/declaration_sale_detail.html', 
                  {'sale_id':id, 'sale': sale})