# cpce_web_app/urls.py

from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from economic_exchanges.views.base_views import ProducerViewSet, ProductViewSet, ProvinceViewSet, SupplierViewSet, CompanyClientViewSet, PersonalClientViewSet, PurchaseViewSet, SaleViewSet, api_root, home, RegisterView, CustomTokenObtainPairView, LogoutView
from rest_framework_simplejwt.views import TokenRefreshView


router = DefaultRouter()
router.register(r'producers', ProducerViewSet)
router.register(r'products', ProductViewSet)
router.register(r'provinces', ProvinceViewSet)
router.register(r'suppliers', SupplierViewSet)
router.register(r'company_clients', CompanyClientViewSet)
router.register(r'personal_clients', PersonalClientViewSet)
router.register(r'purchases', PurchaseViewSet)
router.register(r'sales', SaleViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/auth/register/', RegisterView.as_view(), name='auth-register'),
    path('api/auth/login/', CustomTokenObtainPairView.as_view(), name='auth-login'),
    path('api/auth/logout/', LogoutView.as_view(), name='auth-logout'),
    path('api/auth/token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    path('', home),
]