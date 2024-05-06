from django.contrib import admin

from economic_exchanges.models.producers import Producer
from economic_exchanges.models.products import Product
from economic_exchanges.models.suppliers import Supplier
from economic_exchanges.models.company_clients import CompanyClient
from economic_exchanges.models.personal_clients import PersonalClient
from economic_exchanges.models.purchases import Purchase
from economic_exchanges.models.sales import Sale
from economic_exchanges.models.provinces import Province


# class ProducerAdmin(admin.ModelAdmin):
#     list_display = ('id', 'company_name', 'manager_name', 'address', 'tax_code', 'nrc', 'nat_id', 'email', 'phone_number', 'province', 'product_id')

admin.site.register(Producer)
admin.site.register(Product)
admin.site.register(Supplier)
admin.site.register(CompanyClient)
admin.site.register(PersonalClient)
admin.site.register(Purchase)
admin.site.register(Sale)
admin.site.register(Province)

