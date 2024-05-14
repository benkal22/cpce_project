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
from economic_exchanges.views import ProducerRegisterView, ProducerLoginView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path('dashboard/<int:pk>/', views.dashboard, name='dashboard'),

    # path('product/', views.product_home, name='product-list'),
    # path('product/<int:id>/', views.product_detail, name='product-detail'),
    # PRODUCT
    # path('products/', views.product_list, name='product_list'),
    # path('products/<int:pk>/', views.product_detail, name='product_detail'),
    # path('products/new/', views.product_create, name='product_create'),
    # path('products/<int:pk>/edit/', views.product_update, name='product_update'),
    # path('products/<int:pk>/delete/', views.product_delete, name='product_delete'),

    # PRODUCER
    path('producers/', views.producer_list, name='producer_list'),
    path('producers/<int:pk>/', views.producer_detail, name='producer_detail'),
    path('producers/new/', views.producer_create, name='producer_create'),
    path('producers/<int:pk>/edit/', views.producer_update, name='producer_update'),
    path('producers/<int:pk>/delete/', views.producer_delete, name='producer_delete'),

    path('supplier/', views.supplier_home, name='supplier-list'),
    path('supplier/<int:id>/', views.supplier_detail, name='supplier-detail'),
    path('supplier/add/', views.supplier_create, name='supplier-create'),

    path('client/', views.client_home, name='client-list'),
    path('client/comp<int:id>/', views.client_company_detail, name='client-company-detail'),
    path('client/pers<int:id>/', views.client_personal_detail, name='client-personal-detail'),

    path('declaration/', views.declaration_home, name='purchases-sales'),
    path('declaration/purch<int:id>/', views.declaration_purchase_detail, name='declaration-purchase-detail'),
    path('declaration/sal<int:id>/', views.declaration_sale_detail, name='declaration-sale-detail'),

    path('contact/<int:pk>/', views.contact, name='contact'),   
    path('contact-sent/<int:pk>/', views.contact_sent, name='contact-sent'),

    # Login
    path('accounts/register/', ProducerRegisterView.as_view(), name='register'),
    path('accounts/login/', ProducerLoginView.as_view(), name='login'),
    path('get_product_labels/', views.get_product_labels, name='get_product_labels'),
    # path('profile<int:id>/', views.profile, name='profile'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/profile/', views.profile, name='profile'),
    

    #Others pages
    path('faq/<int:pk>/', views.page_faq, name='faq'),
    

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)