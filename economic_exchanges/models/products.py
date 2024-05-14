from django.db import models

class Product(models.Model):
    sector_code = models.CharField(max_length=20)
    sector_label = models.CharField(max_length=150)
    activity_code = models.CharField(max_length=20)
    activity_label = models.CharField(max_length=150)
    product_code = models.CharField(max_length=20)
    product_label = models.CharField(max_length=150)
    
    def __str__(self):
        return self.product_label
    
    @staticmethod
    def clean_labels():
        # Récupérer tous les enregistrements de Product
        products = Product.objects.all()

        # Parcourir chaque enregistrement et nettoyer les labels
        for product in products:
            product.sector_label = product.sector_label.strip()
            product.activity_label = product.activity_label.strip()
            product.product_label = product.product_label.strip()
            
            # Enregistrer les modifications
            product.save()