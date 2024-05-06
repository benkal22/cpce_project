from django.db import models
from economic_exchanges.models.producers import Producer

#PersonalClient
class PersonalClient(models.Model):
    producer = models.ForeignKey(Producer, on_delete=models.CASCADE, related_name='producer_personal_client')
    # personal_client_id = models.AutoField(primary_key=True)
    personal_client_name = models.fields.CharField(max_length=100)
    address = models.fields.CharField(max_length=255)
    email = models.fields.CharField(max_length=100, null=True)
    phone_number = models.fields.CharField(max_length=20, null=True)
    country = models.fields.CharField(max_length=100)
    province = models.fields.CharField(max_length=100)
    def __str__(self) -> str:
        return f'{self.personal_client_name}'
