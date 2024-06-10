# views.py

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from ..models import Producer, Product, Province, Supplier, CompanyClient, PersonalClient, Purchase, Sale
from ..serializers import ProducerSerializer, ProductSerializer, ProvinceSerializer, SupplierSerializer, CompanyClientSerializer, PersonalClientSerializer, PurchaseSerializer, SaleSerializer
from ..serializers import RegisterSerializer, CustomTokenObtainPairSerializer

from django.shortcuts import redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView

from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView

class ProducerViewSet(viewsets.ModelViewSet):
    queryset = Producer.objects.all()
    serializer_class = ProducerSerializer
    permission_classes = [IsAuthenticated]

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

class ProvinceViewSet(viewsets.ModelViewSet):
    queryset = Province.objects.all()
    serializer_class = ProvinceSerializer
    permission_classes = [IsAuthenticated]

class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    permission_classes = [IsAuthenticated]

class CompanyClientViewSet(viewsets.ModelViewSet):
    queryset = CompanyClient.objects.all()
    serializer_class = CompanyClientSerializer
    permission_classes = [IsAuthenticated]

class PersonalClientViewSet(viewsets.ModelViewSet):
    queryset = PersonalClient.objects.all()
    serializer_class = PersonalClientSerializer
    permission_classes = [IsAuthenticated]

class PurchaseViewSet(viewsets.ModelViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer
    permission_classes = [IsAuthenticated]

class SaleViewSet(viewsets.ModelViewSet):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer
    permission_classes = [IsAuthenticated]

class RegisterView(APIView):
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        if not username or not password:
            return Response({'error': 'Please provide both username and password.'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            user = User.objects.create_user(username=username, password=password)
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_201_CREATED)
        except:
            return Response({'error': 'User already exists.'}, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid credentials.'}, status=status.HTTP_400_BAD_REQUEST)

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        request.user.auth_token.delete()
        logout(request)
        return Response(status=status.HTTP_200_OK)

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'producers': reverse('producer-list', request=request, format=format),
        'products': reverse('product-list', request=request, format=format),
        'provinces': reverse('province-list', request=request, format=format),
        'suppliers': reverse('supplier-list', request=request, format=format),
        'company_clients': reverse('companyclient-list', request=request, format=format),
        'personal_clients': reverse('personalclient-list', request=request, format=format),
        'purchases': reverse('purchase-list', request=request, format=format),
        'sales': reverse('sale-list', request=request, format=format),
    })

def home(request):
    if request.user.is_authenticated:
        return redirect('/api/')
    return redirect('/admin/login/?next=/')

class RegisterView(generics.CreateAPIView):
    queryset = Producer.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer 

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

class LogoutView(generics.GenericAPIView):
    def post(self, request, *args, **kwargs):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
