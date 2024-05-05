from django.db import models

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
