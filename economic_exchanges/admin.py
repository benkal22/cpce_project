# from django.contrib import admin

# from economic_exchanges.models.producers import Producer
# from economic_exchanges.models.products import Product
# from economic_exchanges.models.suppliers import Supplier
# from economic_exchanges.models.company_clients import CompanyClient
# from economic_exchanges.models.personal_clients import PersonalClient
# from economic_exchanges.models.purchases import Purchase
# from economic_exchanges.models.sales import Sale
# from economic_exchanges.models.provinces import Province


# # class ProducerAdmin(admin.ModelAdmin):
# #     list_display = ('id', 'company_name', 'manager_name', 'address', 'tax_code', 'nrc', 'nat_id', 'email', 'phone_number', 'province', 'product_id')

# class ProductAdmin(admin.ModelAdmin):
#     list_display = ('id', 'sector_code', 'sector_label', 'activity_code', 'activity_label', 'product_code', 
#                     'product_label')
    
# class ProductInline(admin.TabularInline):
#     model = Producer.product.through
#     extra = 1

# class ProducerAdmin(admin.ModelAdmin):
#     inlines = [
#         ProductInline,
#     ]

# admin.site.register(Producer, ProducerAdmin)
# # admin.site.register(Product)

# # admin.site.register(Producer)
# admin.site.register(Product, ProductAdmin)
# admin.site.register(Supplier)
# admin.site.register(CompanyClient)
# admin.site.register(PersonalClient)
# admin.site.register(Purchase)
# admin.site.register(Sale)
# admin.site.register(Province)

# admin.py
# admin.py

from django.contrib import admin
from .models import Producer, Product, Province, Supplier, CompanyClient, PersonalClient, Purchase, Sale

admin.site.register(Producer)
admin.site.register(Product)
admin.site.register(Province)
admin.site.register(Supplier)
admin.site.register(CompanyClient)
admin.site.register(PersonalClient)
admin.site.register(Purchase)
admin.site.register(Sale)
