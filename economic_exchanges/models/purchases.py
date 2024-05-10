from django.db import models

from economic_exchanges.models.producers import Producer
from economic_exchanges.models.products import Product
from economic_exchanges.models.suppliers import Supplier

#Achat chez le fournisseur
class Purchase(models.Model):
    # purchase_id = models.AutoField(primary_key=True)
    supplier = models.ForeignKey(Supplier, null=True, on_delete=models.CASCADE, related_name='supplier_purchase')
    producer = models.ForeignKey(Producer, null=True, on_delete=models.CASCADE, related_name='producer_purchase')
    # product = models.ForeignKey(Product, null=True, on_delete=models.CASCADE, related_name='product_purchase')
    product = models.ManyToManyField(Product)
    price = models.fields.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.fields.IntegerField()
    tva = models.fields.DecimalField(max_digits=5, decimal_places=2, null=True)
    date = models.fields.DateField()
    def __str__(self) -> str:
        return f'{self.quantity}'
