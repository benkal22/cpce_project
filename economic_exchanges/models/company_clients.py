from django.db import models
from economic_exchanges.models.products import Product
from economic_exchanges.models.producers import Producer

#CompanyClient
class CompanyClient(models.Model):
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL, related_name='product_company_client')
    producer = models.ForeignKey(Producer, on_delete=models.CASCADE, related_name='producer_company_client')
    # company_client_id = models.AutoField(primary_key=True)
    company_name = models.fields.CharField(max_length=100)
    manager_name = models.fields.CharField(max_length=100)
    address = models.fields.CharField(max_length=255)
    tax_code = models.fields.CharField(max_length=100, null=True)
    nrc = models.fields.CharField(max_length=100, null=True)
    nat_id = models.fields.CharField(max_length=100, null=True)
    email = models.fields.CharField(max_length=100, null=True)
    phone_number = models.fields.CharField(max_length=20, null=True)
    country = models.fields.CharField(max_length=100)
    province = models.fields.CharField(max_length=100)
    def __str__(self) -> str:
        return f'{self.company_name}'
