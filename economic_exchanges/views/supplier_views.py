from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.urls import reverse_lazy, reverse

from economic_exchanges.models.suppliers import Supplier, Producer, Product
from django.http import JsonResponse

from ..forms.supplier_forms import SupplierCreateForm, SupplierEditForm
from economic_exchanges.views.base_views import get_product_labels

#View Fournisseur
def supplier_home(request):
    suppliers = Supplier.objects.all()
    return render(request, 'economic_exchanges/supplier/supplier_list.html', {'suppliers': suppliers})

def supplier_list(request):
    suppliers = Supplier.objects.filter(producer=request.user)
    return render(request, 'economic_exchanges/supplier/supplier_list.html', {'suppliers': suppliers})

# @login_required
# def supplier_detail(request, id):
#     supplier = get_object_or_404(Supplier, id=id, producer=request.user)
#     return render(request, 'economic_exchanges/supplier/supplier_detail.html', {'supplier': supplier})

@login_required
def supplier_detail(request, id):
    producer = get_object_or_404(Producer, id=id)
    suppliers = Supplier.objects.filter(producer=request.user)
    active_tab = request.GET.get('tab', 'detail')
    context = {
        'page_super_title': 'Accueil',
        'page_title': 'Mes fournisseurs',
        'breadcrumb_title': 'Mes fournisseurs',
        'producer': producer,
        'suppliers': suppliers,
        'active_tab': active_tab
    }
    return render(request, 'economic_exchanges/supplier/supplier_list.html', context)

@login_required
def supplier_create(request):
    if request.method == 'POST':
        form = SupplierCreateForm(request.POST)
        if form.is_valid():
            supplier = form.save(commit=False)
            supplier.producer = request.user
            supplier.save()
            form.save_m2m()  # Save many-to-many relationships
            return redirect('supplier_list')
    else:
        form = SupplierCreateForm()
    # return render(request, 'economic_exchanges/supplier/supplier_create.html', {'form': form})
    return render(request, 'economic_exchanges/supplier/supplier_create.html', {
            'form': form,
            'was_validated': 'was-validated' if request.method == 'POST' and not form.is_valid() else '',
        })

@login_required
def supplier_edit(request, id):
    supplier = get_object_or_404(Supplier, id=id, producer=request.user)
    if request.method == 'POST':
        form = SupplierEditForm(request.POST, instance=supplier)
        if form.is_valid():
            form.save()
            return redirect('supplier_detail', id=supplier.id)
    else:
        form = SupplierEditForm(instance=supplier)
    return render(request, 'economic_exchanges/supplier/supplier_form.html', {'form': form})

@login_required
def supplier_delete(request, id):
    supplier = get_object_or_404(Supplier, id=id, producer=request.user)
    if request.method == 'POST':
        supplier.delete()
        return redirect('supplier_list')
    return render(request, 'economic_exchanges/supplier/supplier_confirm_delete.html', {'supplier': supplier})

class SupplierCreateView(CreateView):
    template_name = 'economic_exchanges/supplier/supplier_create.html'
    form_class = SupplierCreateForm
    success_url = reverse_lazy('supplier-detail')
    redirect_field_name = 'next'
    
    # def get_success_url(self):
    #     supplier = self.object  # `self.object` est le producteur nouvellement créé
    #     redirect_to = self.request.GET.get(self.redirect_field_name)
    #     if redirect_to:
    #         return redirect_to
    #     return reverse('supplier-detail', args=[supplier.pk])

    # def get_form_kwargs(self):
    #     kwargs = super().get_form_kwargs()
    #     kwargs['request'] = self.request
    #     return kwargs