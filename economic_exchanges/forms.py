from typing import Any
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from economic_exchanges.models.producers import Producer


class ContactUsForm(forms.Form):
    name = forms.CharField(required=False)
    email = forms.EmailField()
    message = forms.CharField(max_length=1000)

class LoginForm(AuthenticationForm):
    def __init__(self, request: Any = ..., *args: Any, **kwargs: Any) -> None:
        super().__init__(request, *args, **kwargs)
        self.fields['username'].label = "Nom d'utilisateur"
        self.fields['password'].label = "Mot de passe"
        self.fields['password'].widget.attrs.update({'placeholder': 'Entrez votre mot de passe'})

class ProducerRegistrationForm(UserCreationForm):
    class Meta:
        model = Producer
        fields = ('company_name', 'manager_name', 'profile_photo', 'product', 'province', 
                  'address', 'email', 'phone_number', 'username')
        labels = {
            'company_name': "Nom de l'entreprise*",
            'manager_name': "Nom du propriétaire*",
            'profile_photo': "Logo de l'entreprise",
            'product': "Type de produits/services*",
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

    def clean_company_name(self):
        company_name = self.cleaned_data.get('company_name')
        if len(company_name) < 3:
            raise forms.ValidationError("Le nom de l'entreprise doit comporter au moins 3 caractères.")
        return company_name

    # Ajoutez des méthodes clean_<field>() personnalisées pour valider d'autres champs si nécessaire
