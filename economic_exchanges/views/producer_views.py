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

from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView

#Forms lib
from economic_exchanges.forms.producer_forms import ProducerLoginForm, ProductForm, ProducerCreateForm
# from django.forms.forms import modelformset_factory
from ..forms.producer_forms import ProducerForm, ProducerDeleteForm, ProducerEditForm, SettingsForm, PasswordChangeForm

#View producer
# def producer_home(request):
#     producers = Producer.objects.all()
#     return render(request, 'economic_exchanges/producer/producer.html', {'producer': producers})

# def producer_list(request):
#     context = {
#         'page_super_title': 'Accueil',
#         'page_title': 'Les producteurs économiques',
#         'breadcrumb_title': 'Les producteurs économiques',
#     }
#     producers = Producer.objects.all()
#     return render(request, 'economic_exchanges/producer/producer_list.html', {'producers': producers, 'context':context})

def producer_list(request):
    producers = Producer.objects.all()
    context = {
        'page_super_title': 'Accueil',
        'page_title': 'Les producteurs économiques',
        'breadcrumb_title': 'Les producteurs économiques',
        'producers': producers,
    }
    return render(request, 'economic_exchanges/producer/producer_detail.html', context)

# def producer_base(request, id):
#     producer = get_object_or_404(Producer, id=id)
#     context = {
#             'page_super_title': 'Accueil',
#             'page_title': 'Les producteurs économiques',
#             'breadcrumb_title': 'Les producteurs économiques',
#             'producer': producer,
#     }
#     return render(request, 'economic_exchanges/producer/producer_base.html', context)

def producer_detail(request, id):
    producer = get_object_or_404(Producer, id=id)
    active_tab = request.GET.get('tab', 'detail')
    context = {
        'page_super_title': 'Accueil',
        'page_title': 'Les producteurs économiques',
        'breadcrumb_title': 'Les producteurs économiques',
        'producer': producer,
        'active_tab': active_tab
    }
    return render(request, 'economic_exchanges/producer/producer_detail.html', context)

@login_required
def producer_edit(request, id):
    producer = get_object_or_404(Producer, id=id)
    active_tab = request.GET.get('tab', 'edit')

    if request.method == 'POST':
        form = ProducerEditForm(request.POST, request.FILES, instance=producer)
        if form.is_valid():
            form.save()
            return redirect('producer_detail', id=producer.id)
    else:
        form = ProducerEditForm(instance=producer)

    # Pour gérer le chargement dynamique des produits en fonction du secteur d'activité sélectionné
    if 'sector_label' in request.GET:
        sector_label = request.GET['sector_label']
        product_queryset = Product.objects.filter(sector_label=sector_label)
        form.fields['product'].queryset = product_queryset

    return render(request, 'economic_exchanges/producer/producer_edit.html', {
        'form': form,
        'producer': producer,
        'active_tab': active_tab
    })
    
@login_required
def producer_create(request, id):
    producer = get_object_or_404(Producer, id=id)
    active_tab = request.GET.get('tab', 'edit')

    if request.method == 'POST':
        form = ProducerCreateForm(request.POST, request.FILES, instance=producer)
        if form.is_valid():
            form.save()
            return redirect('producer_detail', id=producer.id)
    else:
        form = ProducerEditForm(instance=producer)

    # Pour gérer le chargement dynamique des produits en fonction du secteur d'activité sélectionné
    if 'sector_label' in request.GET:
        sector_label = request.GET['sector_label']
        product_queryset = Product.objects.filter(sector_label=sector_label)
        form.fields['product'].queryset = product_queryset

    return render(request, 'registration/register.html', {
        'form': form,
        'producer': producer,
        'active_tab': active_tab
    })
 
def producer_update_settings(request, id):
    producer = get_object_or_404(Producer, id=id)
    active_tab = request.GET.get('tab', 'settings')
    if request.method == 'POST':
        form = SettingsForm(request.POST, instance=producer)
        if form.is_valid():
            form.save()
            return redirect('producer_detail', id=producer.id)
    return render(request, 'economic_exchanges/producer/producer_detail.html', {
        'producer': producer,
        'active_tab': active_tab
    })

def producer_change_password(request, id):
    producer = get_object_or_404(Producer, id=id)
    active_tab = request.GET.get('tab', 'change_password')
    if request.method == 'POST':
        form = PasswordChangeForm(request.POST)
        if form.is_valid():
            # Handle password change logic here
            return redirect('producer_detail', id=producer.id)
    return render(request, 'economic_exchanges/producer/producer_detail.html', {
        'producer': producer,
        'active_tab': active_tab
    })

@login_required
def producer_delete(request, id):
    producer = get_object_or_404(Producer, id=id)
    active_tab = request.GET.get('tab', 'delete')
    if request.method == 'POST':
        producer.delete()
        return redirect('producer_list')  # Redirige vers la liste des producteurs après suppression
    return render(request, 'economic_exchanges/producer/producer_detail.html', {
        'producer': producer,
        'active_tab': active_tab
    })

@login_required
def home(request):
    return render(request, 'economic_exchanges/dashboard.html')

class ProducerRegisterView(CreateView):
    template_name = 'registration/register.html'
    form_class = ProducerCreateForm
    success_url = reverse_lazy('dashboard')
    redirect_field_name = 'next'
    
    def get_success_url(self):
        producer = self.object  # `self.object` est le producteur nouvellement créé
        redirect_to = self.request.GET.get(self.redirect_field_name)
        if redirect_to:
            return redirect_to
        return reverse('dashboard', args=[producer.pk])

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs
    
def get_product_labels(request):
    sector_label = request.GET.get('sector_label')
    product_labels = list(Product.objects.filter(sector_label=sector_label).values_list('product_label', flat=True).distinct())
    return JsonResponse(product_labels, safe=False)

# LOGIN
class ProducerLoginView(LoginView):
    form_class = ProducerLoginForm
    template_name = 'registration/login.html'
    redirect_field_name = 'next'

    def get_success_url(self):
        producer = self.request.user  # Puisque Producer hérite de AbstractUser
        return reverse('dashboard', args=[producer.pk])
        # return reverse('base', args=[producer.pk])
    
@login_required
def base(request, pk):
    producer = get_object_or_404(Producer, pk=pk)
    # producer = Producer.objects.get(producer=pk)
    return render(request, 'economic_exchanges/dashboard/dashboard.html', {'pk':pk, 'producer': producer})
    
@login_required
def dashboard(request, pk):
    producer = get_object_or_404(Producer, pk=pk)
    # producer = Producer.objects.get(producer=pk)
    return render(request, 'economic_exchanges/dashboard/dashboard.html', {'pk':pk, 'producer': producer})

@login_required
def load_products(request):
    sector_label = request.GET.get('sector_label')
    products = Product.objects.filter(sector_label=sector_label).values('id', 'product_label')
    return JsonResponse(list(products), safe=False)