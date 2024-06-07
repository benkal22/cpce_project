
#Http lib
from django.http import HttpResponse
from django.http import JsonResponse

#Models lib
from economic_exchanges.models.producers import Producer
from economic_exchanges.models.products import Product
from economic_exchanges.models.company_clients import CompanyClient
from economic_exchanges.models.personal_clients import PersonalClient

from django.shortcuts import render, redirect, get_object_or_404
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