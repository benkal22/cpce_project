#Models lib
from economic_exchanges.models.suppliers import Supplier

from django.shortcuts import render, redirect, get_object_or_404

#View Fournisseur
def supplier_home(request):
    suppliers = Supplier.objects.all()
    return render(request, 'economic_exchanges/supplier/supplier_list.html', {'suppliers': suppliers})

def supplier_detail(request, id):
    supplier = Supplier.objects.get(supplier_id=id)
    return render(request, 'economic_exchanges/supplier/supplier_detail.html',
                  {'id': id, 'supplier': supplier})
def supplier_create(request):
    return render(request, 'economic_exchanges/supplier/supplier_list.html')

