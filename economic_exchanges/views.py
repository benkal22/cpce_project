from django.http import HttpResponse

from economic_exchanges.models.producers import Producer
from economic_exchanges.models.products import Product
from economic_exchanges.models.suppliers import Supplier
from economic_exchanges.models.company_clients import CompanyClient
from economic_exchanges.models.personal_clients import PersonalClient
from economic_exchanges.models.purchases import Purchase
from economic_exchanges.models.sales import Sale

from django.shortcuts import render, redirect
from economic_exchanges.forms import ContactUsForm, LoginForm
from django.core.mail import send_mail
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

from django.urls import reverse_lazy
from economic_exchanges.forms import ProducerRegistrationForm
from django.views.generic import CreateView

#Dashboard
def dashboard(request):
    return render(request, 'economic_exchanges/dashboard/dashboard.html', )

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

def producer_detail(request, id):
    producer = Producer.objects.get(producer_id=id)
    return render(request, 
                  'economic_exchanges/producer/producer_detail.html',
                  {'id': id, 'producer': producer})

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
def contact(request):
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
                  'economic_exchanges/contact/contact.html', {'form': form})

def contact_sent(request):
    return render(request, 'economic_exchanges/contact/contact_sent.html')

# Account View
def register_page(request):
    form = ProducerRegistrationForm()
    message = ''
    if request.method == 'POST':
        form = ProducerRegistrationForm(request.POST)
        print("Producer c'est BON")

        if form.is_valid():
            print("Form isValid c'est BON")

            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            if user is not None:
                print(f'Username: {username} et Passwor: {password}')
                login(request, user)
                message = f'Bonjour  {user.username}, votre compte a été créé avec succès !'
            # messages.success(request, f'Bonjour {username}, votre compte a été créé avec succès !')
                return redirect('dashboard')
            else:
                print('Aucun username et password')
                print(form.errors)
                message ='Identifiants invalides'
    
    return render(request, 'registration/register.html', {'form': form, 'message': message})

def profile(request):
    return render(request, 'registration/profile.html')

@login_required
def home(request):
    return render(request, 'economic_exchanges/dashboard.html')

class ProducerRegisterView(CreateView):
    template_name = 'registration/register.html'
    form_class = ProducerRegistrationForm
    success_url = reverse_lazy('dashboard')
    #Champ de redirection
    redirect_field_name = 'next'

    def get_success_url(self) -> str:
        redirect_to = self.request.GET.get(self.redirect_field_name)
        if redirect_to:
            return redirect_to
        return super().get_success_url()


#Faq
def page_faq(request):
    return render(request, 'others_pages/faq.html', )

