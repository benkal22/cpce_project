from django.db import models
from economic_exchanges.models.products import Product

#Producer model
class Producer(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_producer')
    producer_id = models.AutoField(primary_key=True)
    company_name = models.fields.CharField(max_length=100)
    manager_name = models.fields.CharField(max_length=100)
    addresse = models.fields.CharField(max_length=255)
    tax_code = models.fields.CharField(max_length=100,  null=True)
    nrc = models.fields.CharField(max_length=100, null=True)
    nat_id = models.fields.CharField(max_length=100, null=True)
    email = models.fields.CharField(max_length=100, null=True)
    phone_number = models.fields.CharField(max_length=20)
    province = models.fields.CharField(max_length=100)
    def __str__(self) -> str:
        return f'{self.company_name}'