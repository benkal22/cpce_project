# views.py

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

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
