from django.db import models
from economic_exchanges.models.products import Product
from django import forms 

#Supplier model
class Supplier(models.Model):
    product_id = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL, related_name='product_supplier')
    supplier_id = models.AutoField(primary_key=True)
    company_name = models.fields.CharField(max_length=100)
    manager_name = models.fields.CharField(max_length=100)
    address = models.fields.CharField(max_length=255)
    tax_code = models.fields.CharField(max_length=100, null=True)
    nrc = models.fields.CharField(max_length=100, null=True)
    nat_id = models.fields.CharField(max_length=100, null=True)
    email = models.fields.CharField(max_length=100, null=True)
    phone_number = models.fields.CharField(max_length=20)
    country = models.fields.CharField(max_length=100)
    province = models.fields.CharField(max_length=100)
    def __str__(self) -> str:
        return f'{self.company_name}'
    
#SupplierForm
class SupplierForm(forms.Form):
    # product_id = forms.ForeignKey(Product, null=True, on_delete=forms.SET_NULL, related_name='product_supplier')
    # supplier_id = forms.AutoField(primary_key=True)
    company_name = forms.CharField(max_length=100)
    manager_name = forms.CharField(max_length=100)
    address = forms.CharField(max_length=255)
    tax_code = forms.CharField(max_length=100)
    nrc = forms.CharField(max_length=100)
    nat_id = forms.CharField(max_length=100)
    email = forms.CharField(max_length=100)
    phone_number = forms.CharField(max_length=20)
    country = forms.CharField(max_length=100)
    province = forms.CharField(max_length=100)
