"""
URL configuration for cpce_web_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from economic_exchanges import views
from django.urls import path, include
from economic_exchanges.views import base_views
from economic_exchanges.views import client_views
from economic_exchanges.views import contact_views
from economic_exchanges.views import declaration_views
from economic_exchanges.views import producer_views
from economic_exchanges.views import product_views
from economic_exchanges.views import supplier_views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path('dashboard/<int:pk>/', base_views.dashboard, name='dashboard'),

    path('products/<int:pk>/', product_views.product_detail, name='product_detail'),
    path('get_product_labels/', base_views.get_product_labels, name='get_product_labels'),
    
    
    # Login
    path('accounts/register/', producer_views.ProducerRegisterView.as_view(), name='register'),
    path('accounts/login/', producer_views.ProducerLoginView.as_view(), name='login'),
    path('get_product_labels/', producer_views.get_product_labels, name='get_product_labels'),
    path('accounts/', include('django.contrib.auth.urls')),
    
    # PRODUCER
    # path('producers/', producer_views.producer_list, name='producer_list'),
    path('producers/<int:id>/', producer_views.producer_detail, name='producer_detail'),
    # path('accounts/register/', producer_views.producer_create, name='register'),
    path('producers/<int:id>/edit/', producer_views.producer_edit, name='producer_edit'),
    path('producer/<int:id>/settings/', producer_views.producer_update_settings, name='producer_settings'),
    path('producer/<int:id>/change_password/', producer_views.producer_change_password, name='producer_change_password'),
    path('producer/<int:id>/delete/', producer_views.producer_delete, name='producer_delete'),
    # path('get_product_labels/', producer_views.get_product_labels, name='get_product_labels'),
    path('ajax/load-products/', producer_views.load_products, name='ajax_load_products'),

    #FOURNISSEURS
    path('suppliers/', supplier_views.supplier_list, name='supplier-list'),
    path('suppliers/<int:id>/', supplier_views.supplier_detail, name='supplier-detail'),
    path('suppliers/new/', supplier_views.SupplierCreateView.as_view(), name='supplier-create'),
    # path('suppliers/new/', supplier_views.supplier_create, name='supplier-create'),
    path('suppliers/<int:id>/edit/', supplier_views.supplier_edit, name='supplier-edit'),
    path('suppliers/<int:id>/delete/', supplier_views.supplier_delete, name='supplier-delete'),

    path('client/', client_views.client_home, name='client-list'),
    path('client/comp<int:id>/', client_views.client_company_detail, name='client-company-detail'),
    path('client/pers<int:id>/', client_views.client_personal_detail, name='client-personal-detail'),

    path('declaration/', declaration_views.declaration_home, name='purchases-sales'),
    path('declaration/purch<int:id>/', declaration_views.declaration_purchase_detail, name='declaration-purchase-detail'),
    path('declaration/sal<int:id>/', declaration_views.declaration_sale_detail, name='declaration-sale-detail'),

    path('contact/<int:pk>/', contact_views.contact, name='contact'),   
    path('contact-sent/<int:pk>/', contact_views.contact_sent, name='contact-sent'),

    #Others pages
    path('faq/<int:pk>/', base_views.page_faq, name='faq'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)