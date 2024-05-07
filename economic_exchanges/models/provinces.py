from django.db import models

#26 Provinces de la RDC
class Province(models.Model):
    # province = models.AutoField(primary_key=True)
    name = models.fields.CharField(max_length=150)
    chef_lieu = models.fields.CharField(null=True, max_length=150)
    superficie= models.fields.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    population = models.fields.IntegerField(blank=True, null=True) 
    rank =  models.fields.CharField(max_length=150, blank=True, null=True)
    def __str__(self) -> str:
        return f'{self.name}'