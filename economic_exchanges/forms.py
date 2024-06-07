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
            'confirm_password': forms.PasswordInput,
            'profile_photo': forms.ClearableFileInput(attrs={
                'alt': 'Profile Photo',
                'class': 'rounded-circle'
            }),
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


class ProducerForm(forms.ModelForm):
    product_label = forms.ChoiceField(choices=[], label="Produit*") 
    sector_label = forms.ChoiceField(choices=[], label="Secteur d'activité*")  
    
    class Meta:
        model = Producer
        fields = ['company_name', 'manager_name', 'profile_photo',
                  'address', 'tax_code', 'nrc', 'nat_id', 'phone_number', 'province', 'sector_label', 'product_label']
        
        labels = {
            'company_name': "Nom de l'entreprise*",
            'manager_name': "Nom du propriétaire*",
            'sector_label': "Secteur d'activité*",
            'product_label': "Produit*",
            'address': "Adresse de l'entreprise*",
            'phone_number': "Votre numéro de téléphone*",
            'province': "Province de votre entreprise*",
        }
        
        widgets = {
            'profile_photo': forms.ClearableFileInput(attrs={
                'class': 'form-control',
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Fill sector_label field with choices available from database
        sector_labels_choices = [(label, label) for label in Product.objects.values_list('sector_label', flat=True).distinct()]
        self.fields['sector_label'].choices = sector_labels_choices
        
        # Load product_labels if instance is already created
        if self.instance.pk:
            product_labels_choices = [(label, label) for label in Product.objects.filter(sector_label=self.instance.sector_label).values_list('product_label', flat=True).distinct()]
            self.fields['product_label'].choices = product_labels_choices
        else:
            self.fields['product_label'].choices = []

    def clean(self):
        cleaned_data = super().clean()
        sector_label = cleaned_data.get('sector_label')
        product_label = cleaned_data.get('product_label')

        if sector_label and product_label:
            # Validate that the product_label belongs to the selected sector_label
            if not Product.objects.filter(sector_label=sector_label, product_label=product_label).exists():
                self.add_error('product_label', f"Le produit '{product_label}' n'appartient pas au secteur '{sector_label}'.")
        
        return cleaned_data

class ProducerEditForm(forms.ModelForm):
    product = forms.ModelMultipleChoiceField(
        queryset=Product.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label="Produits*"
    )
    sector_label = forms.ChoiceField(choices=[], label="Secteur d'activité*")

    class Meta:
        model = Producer
        fields = ['company_name', 'manager_name', 'profile_photo', 'address', 'tax_code', 'nrc', 'nat_id', 'phone_number', 'province', 'sector_label', 'product']
        labels = {
            'company_name': "Nom de l'entreprise*",
            'manager_name': "Nom du propriétaire*",
            'sector_label': "Secteur d'activité*",
            'product': "Produits*",
            'address': "Adresse de l'entreprise*",
            'phone_number': "Votre numéro de téléphone*",
            'province': "Province de votre entreprise*",
        }
        widgets = {
            'profile_photo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'product': forms.CheckboxSelectMultiple,
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Fill sector_label field with choices available from database
        sector_labels_choices = [(label, label) for label in Product.objects.values_list('sector_label', flat=True).distinct()]
        self.fields['sector_label'].choices = sector_labels_choices
        
        # Set initial products if instance is already created
        if self.instance.pk:
            self.fields['product'].initial = self.instance.product.all()

    def clean_sector_label(self):
        sector_label = self.cleaned_data.get('sector_label')
        if Producer.objects.filter(sector_label=sector_label).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError(f"Le secteur '{sector_label}' est déjà utilisé par un autre producteur.")
        return sector_label

    def save(self, commit=True):
        producer = super().save(commit=False)
        producer.sector_label = self.cleaned_data['sector_label']
        
        if commit:
            producer.save()
            self.save_m2m()  # Save the many-to-many data for the form
        
        return producer
    
# class ProducerEditForm(forms.ModelForm):
#     # edit_producer = forms.BooleanField(widget=forms.HiddenInput, initial=True)
    
#     product_label = forms.ChoiceField(choices=[], label="Produit*") 
#     sector_label = forms.ChoiceField(choices=[], label="Secteur d'activité*")  
    
#     class Meta:
#         model = Producer
#         fields = ['company_name', 'manager_name', 'profile_photo',
#                   'address', 'tax_code', 'nrc', 'nat_id', 'phone_number', 'province', 'sector_label', 'product_label']
        
#         labels = {
#             'company_name': "Nom de l'entreprise*",
#             'manager_name': "Nom du propriétaire*",
#             'sector_label': "Secteur d'activité*",
#             'product_label': "Produit*",
#             'address': "Adresse de l'entreprise*",
#             'phone_number': "Votre numéro de téléphone*",
#             'province': "Province de votre entreprise*",
#         }
        
#         widgets = {
#             'profile_photo': forms.ClearableFileInput(attrs={
#                 'class': 'form-control',
#             }),
#             'product': forms.CheckboxSelectMultiple,
#         }

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
        
#         # Fill sector_label field with choices available from database
#         sector_labels_choices = [(label, label) for label in Product.objects.values_list('sector_label', flat=True).distinct()]
#         self.fields['sector_label'].choices = sector_labels_choices
        
#         # Load product_labels if instance is already created
#         if self.instance.pk:
#             product_labels_choices = [(label, label) for label in Product.objects.filter(sector_label=self.instance.sector_label).values_list('product_label', flat=True).distinct()]
#             self.fields['product_label'].choices = product_labels_choices
#         else:
#             self.fields['product_label'].choices = []

#     def clean(self):
#         cleaned_data = super().clean()
#         sector_label = cleaned_data.get('sector_label')
#         product_label = cleaned_data.get('product_label')

#         if sector_label and product_label:
#             # Validate that the product_label belongs to the selected sector_label
#             if not Product.objects.filter(sector_label=sector_label, product_label=product_label).exists():
#                 self.add_error('product_label', f"Le produit '{product_label}' n'appartient pas au secteur '{sector_label}'.")
        
#         return cleaned_data

class ProducerDeleteForm(forms.ModelForm):
    delete_producer = forms.BooleanField(widget=forms.HiddenInput, initial=True)
    class Meta:
        model = Producer
        fields = []

class SettingsForm(forms.ModelForm):
    class Meta:
        model = Producer
        # fields = ['notification_settings']  # Exemple de champ
        fields = []  # Exemple de champ

class PasswordChangeForm(forms.Form):
    current_password = forms.CharField(label='Mot de passe actuel', widget=forms.PasswordInput)
    new_password = forms.CharField(label='Nouveau mot de passe', widget=forms.PasswordInput)
    confirm_new_password = forms.CharField(label='Confirmer le nouveau mot de passe', widget=forms.PasswordInput) 

# Formulaire pour un produit individuel
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_label']
        
    