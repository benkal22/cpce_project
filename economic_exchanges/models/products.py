from django.db import models

#Nomenclature/Secteur d'activité model
class Product(models.Model):
    # product_id = models.AutoField(primary_key=True)
    sector_code = models.fields.CharField(max_length=20)
    sector_label = models.fields.CharField(max_length=150)
    activity_code = models.fields.CharField(max_length=20)
    activity_label = models.fields.CharField(max_length=150)
    product_code = models.fields.CharField(max_length=20)
    product_label = models.fields.CharField(max_length=150)
    def __str__(self) -> str:
        return f'{self.product_label}'