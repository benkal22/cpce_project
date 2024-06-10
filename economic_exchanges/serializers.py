# serializers.py

from rest_framework import serializers
from .models import Producer, Product, Province, Supplier, CompanyClient, PersonalClient, Purchase, Sale

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class ProducerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producer
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class ProvinceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Province
        fields = '__all__'

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'

class CompanyClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyClient
        fields = '__all__'

class PersonalClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalClient
        fields = '__all__'

class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase
        fields = '__all__'

class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = '__all__'

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producer
        fields = ('username', 'password', 'email', 'company_name', 'manager_name', 'sector_label', 'address', 'phone_number', 'province')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = Producer.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email'],
            company_name=validated_data['company_name'],
            manager_name=validated_data['manager_name'],
            sector_label=validated_data['sector_label'],
            address=validated_data['address'],
            phone_number=validated_data['phone_number'],
            province=validated_data['province'],
        )
        return user

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        token['company_name'] = user.company_name
        return token