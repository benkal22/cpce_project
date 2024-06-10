from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework.routers import DefaultRouter
from economic_exchanges.views.base_views import ProducerViewSet, ProductViewSet, ProvinceViewSet, SupplierViewSet, CompanyClientViewSet, PersonalClientViewSet, PurchaseViewSet, SaleViewSet


router = routers.DefaultRouter()

router.register(r'producers', ProducerViewSet)
router.register(r'products', ProductViewSet)
router.register(r'provinces', ProvinceViewSet)
router.register(r'suppliers', SupplierViewSet)
router.register(r'company_clients', CompanyClientViewSet)
router.register(r'personal_clients', PersonalClientViewSet)
router.register(r'purchases', PurchaseViewSet)
router.register(r'sales', SaleViewSet)