from django.db import models

#Nomenclature/Secteur d'activité model
class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    sector_code = models.fields.CharField(max_length=20)
    sector_label = models.fields.CharField(max_length=150)
    activity_code = models.fields.CharField(max_length=20)
    activity_label = models.fields.CharField(max_length=150)
    product_code = models.fields.CharField(max_length=20)
    product_label = models.fields.CharField(max_length=150)
    def __str__(self) -> str:
        return f'{self.product_label}'

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
    
#Customer : 2 types of clients : Companies and personal clients 
#CompanyClient
class CompanyClient(models.Model):
    product_id = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL, related_name='product_company_client')
    company_client_id = models.AutoField(primary_key=True)
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

#PersonalClient
class PersonalClient(models.Model):
    personal_client_id = models.AutoField(primary_key=True)
    personal_client_name = models.fields.CharField(max_length=100)
    address = models.fields.CharField(max_length=255)
    email = models.fields.CharField(max_length=100, null=True)
    phone_number = models.fields.CharField(max_length=20, null=True)
    country = models.fields.CharField(max_length=100)
    province = models.fields.CharField(max_length=100)
    def __str__(self) -> str:
        return f'{self.personal_client_name}'

#Tous les clients
# class Client(models.Model):
#     client_id = models.AutoField(primary_key=True)
#     client_type = models.fields.CharField(max_length=20)

#Achat chez le fournisseur
class Purchase(models.Model):
    purchase_id = models.AutoField(primary_key=True)
    supplier_id = models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name='supplier_purchase')
    producer_id = models.ForeignKey(Producer, on_delete=models.CASCADE, related_name='producer_purchase')
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_purchase')
    price = models.fields.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.fields.IntegerField()
    tva = models.fields.DecimalField(max_digits=5, decimal_places=2, null=True)
    date = models.fields.DateField()
    def __str__(self) -> str:
        return f'{self.quantity}'

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





