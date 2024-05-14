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
from economic_exchanges.forms import ContactUsForm, ProducerLoginForm, ProductForm, ProducerRegistrationForm
from django.forms import modelformset_factory
from .forms import ProducerForm

#View product / Secteur d'activité économique
def product_home(request):
    products = Product.objects.all()
    return render(request, 'economic_exchanges/product/product_list.html', {'products': products})

def product_detail(request, id):
    product = Product.objects.get(product_id=id)
    return render(request, 'economic_exchanges/product/product_detail.html', 
                  {'product_id':id, 'product': product})

#View producer
def producer_home(request):
    producers = Producer.objects.all()
    return render(request, 'economic_exchanges/producer/producer.html', {'producer': producers})

# def producer_detail(request, id):
#     producer = Producer.objects.get(producer_id=id)
#     return render(request, 
#                   'economic_exchanges/producer/producer_detail.html',
#                   {'id': id, 'producer': producer})
# .......
def producer_list(request):
    context = {
        'page_super_title': 'Accueil',
        'page_title': 'Les producteurs économiques',
        'breadcrumb_title': 'Les producteurs économiques',
    }
    producers = Producer.objects.all()
    return render(request, 'economic_exchanges/producer/producer_list.html', {'producers': producers, 'context':context})

def producer_detail(request, pk):
    producer = get_object_or_404(Producer, pk=pk)
    return render(request, 'economic_exchanges/producer/producer_detail.html', {'producer': producer})

def producer_create(request):
    if request.method == 'POST':
        form = ProducerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('economic_exchanges/producer/producer_list')
    else:
        form = ProducerForm()
    return render(request, 'economic_exchanges/producer/producer_form.html', {'form': form})

def producer_update(request, pk):
    producer = get_object_or_404(Producer, pk=pk)
    if request.method == 'POST':
        form = ProducerForm(request.POST, request.FILES, instance=producer)
        if form.is_valid():
            form.save()
            return redirect('economic_exchanges/producer/producer_list')
    else:
        form = ProducerForm(instance=producer)
    return render(request, 'economic_exchanges/producer/producer_form.html', {'form': form})

def producer_delete(request, pk):
    producer = get_object_or_404(Producer, pk=pk)
    if request.method == 'POST':
        producer.delete()
        return redirect('economic_exchanges/producer/producer_list')
    return render(request, 'economic_exchanges/producer/producer_confirm_delete.html', {'producer': producer})


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


#View Client
def client_home(request):
    companyClients = CompanyClient.objects.all()
    personalClients = PersonalClient.objects.all()
    return render(request, 'economic_exchanges/client/client_list.html', {'companyClients': companyClients, 'personalClients': personalClients})

def client_company_detail(request, id):
    companyClient = CompanyClient.objects.get(company_client_id=id)
    return render(request, 'economic_exchanges/client/client_company_detail.html',
                  {'company_client_id': id, 'companyClient': companyClient})

def client_personal_detail(request, id):
    personalClient = PersonalClient.objects.get(personal_client_id=id)
    return render(request, 'economic_exchanges/client/client_personal_detail.html',
                  {'personal_client_id':id, 'personalClient': personalClient})

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
#Contact Form
def contact(request, pk):
    producer = get_object_or_404(Producer, pk=pk)
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            send_mail(
                subject=f'Message from {name or 'anonyme'} via CPCE App Contact Us Form',
                message=message,
                from_email=email,
                recipient_list = ['benkalsoft@gmail.com']
            )
            return redirect('contact-sent')
    else:
        form = ContactUsForm()
    return render(request,
                  'economic_exchanges/contact/contact.html', {'form': form, 'pk':pk, 'producer': producer})

def contact_sent(request, pk):
    producer = get_object_or_404(Producer, pk=pk)
    
    return render(request, 'economic_exchanges/contact/contact_sent.html', {'pk':pk, 'producer': producer})

# Account View
def profile(request):
    return render(request, 'registration/profile.html')

@login_required
def home(request):
    return render(request, 'economic_exchanges/dashboard.html')

class ProducerRegisterView(CreateView):
    template_name = 'registration/register.html'
    form_class = ProducerRegistrationForm
    success_url = reverse_lazy('dashboard')
    redirect_field_name = 'next'
    
    def get_success_url(self):
        redirect_to = self.request.GET.get(self.redirect_field_name)
        if redirect_to:
            return redirect_to
        return super().get_success_url()

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
    
#Faq
def page_faq(request, pk):
    producer = get_object_or_404(Producer, pk=pk)
    return render(request, 'others_pages/faq.html', {'pk':pk, 'producer': producer})

