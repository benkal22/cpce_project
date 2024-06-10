from django.db import models
from economic_exchanges.models.products import Product
from economic_exchanges.models.producers import Producer
from economic_exchanges.models.provinces import Province
from django import forms 

#Supplier model
class Supplier(models.Model):
    product = models.ManyToManyField(Product, blank=True) 
    producer = models.ForeignKey(Producer, null=True, on_delete=models.CASCADE, related_name='producer_supplier')
    company_name = models.CharField(max_length=100)
    manager_name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    tax_code = models.CharField(max_length=100, null=True)
    nrc = models.CharField(max_length=100, null=True)
    nat_id = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100, null=True)
    phone_number = models.CharField(max_length=20)
    country = models.CharField(max_length=100)
    province = models.ForeignKey(Province, null=True, on_delete=models.CASCADE, related_name='supplier_province')
    sector_label = models.CharField(blank=True, null=True, max_length=200)
    
    def __str__(self) -> str:
        return f'{self.company_name}'
    

