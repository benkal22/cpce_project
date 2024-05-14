from typing import Any
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from economic_exchanges.models.producers import Producer
from economic_exchanges.models.products import Product
# from django.forms import inlineformset_factory
from django.forms import modelformset_factory
from django.http import JsonResponse
import json 

class ContactUsForm(forms.Form):
    name = forms.CharField(required=False)
    email = forms.EmailField()
    message = forms.CharField(max_length=1000)

class ProducerLoginForm(AuthenticationForm):
    pass

class ProducerRegistrationForm(UserCreationForm):
    sector_label = forms.ChoiceField(choices=[], label="Secteur d'activité*")  
    product_label = forms.ChoiceField(choices=[], label="Produit*") 
    # Remplissage initial des choices pour sector_label
    
    class Meta:
        model = Producer
        fields = ('company_name', 'manager_name','province',
                  'address', 'email', 'phone_number', 'username')
        labels = {
            'company_name': "Nom de l'entreprise*",
            'manager_name': "Nom du propriétaire*",
            'sector_label': "Secteur d'activité*",
            'profile_photo': "Logo de l'entreprise",
            'address': "Adresse de l'entreprise*",
            'email': "Votre email*",
            'phone_number': "Votre numéro de téléphone*",
            'province': "Province de votre entreprise*",
            'username': "Nom d'utilisateur*",
        }
        widgets = {
            'password': forms.PasswordInput,
            'confirm_password': forms.PasswordInput
        }

    def __init__(self, request=None, *args, **kwargs):
        self.request = request
        super().__init__(*args, **kwargs)
        if request:
            # Remplissez le champ sector_labels avec les choix disponibles depuis la base de données
            sector_labels_choices = [(label, label) for label in Product.objects.values_list('sector_label', flat=True).distinct()]
            self.fields['sector_label'].choices = sector_labels_choices

            sector_label_choiced = request.GET.get('sector_label')
           

            product_labels_choices = [(label, label) for label in Product.objects.filter(sector_label=sector_label_choiced).values_list('product_label', flat=True).distinct()]
            self.fields['product_label'].choices = product_labels_choices

            # Vérifier que 'sector_label_choiced' a une valeur correcte
            if sector_label_choiced:
                product_labels_choices = [(label, label) for label in Product.objects.filter(sector_label="ENSEIGNEMENT").values_list('product_label', flat=True).distinct()]
                self.fields['product_label'].choices = product_labels_choices
                print("Valeur de 'sector_label' :", sector_label_choiced)
                print("Type de 'sector_label_choiced' :", type(sector_label_choiced))

# Formulaire pour un produit individuel
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_label']

class ProducerForm(forms.ModelForm):  
    class Meta:
        model = Producer
        fields = ['company_name', 'manager_name', 'profile_photo', 
                  'address', 'tax_code', 'nrc', 'nat_id', 'phone_number', 'province', 'product', 'sector_label']
        
    