from django.db import models
from django.contrib.auth.models import AbstractUser
from economic_exchanges.models.products import Product
from economic_exchanges.models.provinces import Province

#Producer model défini comme utilisateur de l'application
class Producer(AbstractUser):
    # product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL, related_name='product_producer')
    company_name = models.fields.CharField(max_length=100)
    manager_name = models.fields.CharField(max_length=100)
    profile_photo = models.ImageField(verbose_name='Photo de profil entreprise', blank=True, null=True)
    address = models.fields.CharField(max_length=255)
    tax_code = models.fields.CharField(max_length=100, blank=True, null=True)
    nrc = models.fields.CharField(max_length=100, blank=True, null=True)
    nat_id = models.fields.CharField(max_length=100, blank=True, null=True)
    phone_number = models.fields.CharField(max_length=20)
    province = models.ForeignKey(Province, null=True, on_delete=models.CASCADE, related_name='producer_province')
    product = models.ManyToManyField(Product, blank=True) 
    sector_label =  models.fields.CharField(blank=True, null=True, max_length=200)
    about =  models.fields.CharField(blank=True, null=True, max_length=1000)

    def __str__(self) -> str:
        return f'{self.company_name}'