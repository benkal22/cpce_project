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
from ..forms import ProducerForm



# Account View
# def profile(request):
#     return render(request, 'registration/profile.html')

@login_required
def home(request):
    return render(request, 'economic_exchanges/dashboard.html')

# CREATION COMPTE PRODUCTEUR
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

# LOGIN COMPTE PRODUCTEUR
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

# OTHERS VIEWS
#   Faq
def page_faq(request, pk):
    producer = get_object_or_404(Producer, pk=pk)
    return render(request, 'others_pages/faq.html', {'pk':pk, 'producer': producer})

