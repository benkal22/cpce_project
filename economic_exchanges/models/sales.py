from django.db import models

from economic_exchanges.models.producers import Producer
from economic_exchanges.models.products import Product
from economic_exchanges.models.company_clients import CompanyClient
from economic_exchanges.models.personal_clients import PersonalClient

#Vente au client
class Sale(models.Model):
    sale_id = models.AutoField(primary_key=True)
    producer_id = models.ForeignKey(Producer, on_delete=models.CASCADE, related_name='producer_sale')
    # client_id = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='client_sale')
    company_id = models.ForeignKey(CompanyClient, on_delete=models.CASCADE, related_name='company_client_sale', blank=True, null=True)
    personal_client_id = models.ForeignKey(PersonalClient, on_delete=models.CASCADE, related_name='personal_client_sale', blank=True, null=True)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='secteur_activite')
    price = models.fields.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.fields.IntegerField()
    tva = models.fields.DecimalField(max_digits=5, decimal_places=2)
    date = models.fields.DateField()
    def __str__(self) -> str:
        return f'{self.quantity}'

