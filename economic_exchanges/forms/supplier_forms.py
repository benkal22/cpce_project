from typing import Any
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from economic_exchanges.models.suppliers import Supplier
from economic_exchanges.models.products import Product

from django.forms import modelformset_factory
from django.http import JsonResponse
import json 
 
class SupplierCreateForm(forms.ModelForm):
    sector_label = forms.ChoiceField(choices=[], label="Secteur d'activité*")
    # product = forms.ModelMultipleChoiceField(
    #     queryset=Product.objects.none(),
    #     widget=forms.CheckboxSelectMultiple,
    #     label="Produits*",
    #     required=False
    # )

    class Meta:
        model = Supplier
        fields = [
            'company_name', 'manager_name', 'address', 'tax_code', 
            'nrc', 'nat_id', 'phone_number', 'province', 'sector_label',
        ]
        labels = {
            'company_name': "Nom de l'entreprise*",
            'manager_name': "Nom du propriétaire*",
            'sector_label': "Secteur d'activité*",
            # 'product': "Produits*",
            'address': "Adresse de l'entreprise*",
            'phone_number': "Votre numéro de téléphone*",
            'province': "Province de votre entreprise*",
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        sector_labels_choices = [(label, label) for label in Product.objects.values_list('sector_label', flat=True).distinct()]
        self.fields['sector_label'].choices = sector_labels_choices

        # Initialisation du queryset des produits si un secteur d'activité est déjà sélectionné
        # if self.instance.pk and self.instance.sector_label:
        #     product_queryset = Product.objects.filter(sector_label=self.instance.sector_label)
        #     self.fields['product'].queryset = product_queryset
        #     self.fields['product'].initial = self.instance.product.all()
        # else:
        #     self.fields['product'].queryset = Product.objects.none()

    def save(self, commit=True):
        supplier = super().save(commit=False)
        supplier.sector_label = self.cleaned_data['sector_label']
        
        if commit:
            supplier.save()
            self.save_m2m()  # Save the many-to-many data for the form
        
        return supplier


class SupplierEditForm(forms.ModelForm):
    # sector_label = forms.ChoiceField(choices=[], label="Secteur d'activité*")
    sector_label = forms.ChoiceField(choices=[], label="Secteur d'activité*")
    product = forms.ModelMultipleChoiceField(
        queryset=Product.objects.none(),
        widget=forms.CheckboxSelectMultiple,
        label="Produits*",
        required=False
    )

    class Meta:
        model = Supplier
        fields = [
            'company_name', 'manager_name', 'address', 'tax_code', 
            'nrc', 'nat_id', 'phone_number', 'province', 'sector_label', 'product'
        ]
        labels = {
            'company_name': "Nom de l'entreprise*",
            'manager_name': "Nom du propriétaire*",
            'sector_label': "Secteur d'activité*",
            'product': "Produits*",
            'address': "Adresse de l'entreprise*",
            'phone_number': "Votre numéro de téléphone*",
            'province': "Province de votre entreprise*",
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        sector_labels_choices = [(label, label) for label in Product.objects.values_list('sector_label', flat=True).distinct()]
        self.fields['sector_label'].choices = sector_labels_choices

        if self.instance.pk and self.instance.sector_label:
            product_queryset = Product.objects.filter(sector_label=self.instance.sector_label)
            self.fields['product'].queryset = product_queryset
            self.fields['product'].initial = self.instance.product.all()

    def save(self, commit=True):
        supplier = super().save(commit=False)
        supplier.sector_label = self.cleaned_data['sector_label']
        
        if commit:
            supplier.save()
            self.save_m2m()  # Save the many-to-many data for the form
        
        return supplier

# class SupplierDeleteForm(forms.ModelForm):
#     delete_supplier = forms.BooleanField(widget=forms.HiddenInput, initial=True)
#     class Meta:
#         model = Supplier
#         fields = []
