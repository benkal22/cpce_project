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

#By Producer
class ProducerRegistrationForm(forms.ModelForm):
    username = forms.CharField(label="Nom d'utilisateur*")
    password = forms.CharField(label='Mot de passe*', widget=forms.PasswordInput)
    confirm_password = forms.CharField(label='Confirmer le mot de passe*', widget=forms.PasswordInput)
    class Meta:
        model = Producer
        fields = ('company_name', 'manager_name', 'profile_photo', 'product', 'province', 'address', 'tax_code', 
                  'nrc', 'nat_id', 'email', 'phone_number','username', 'password', 'confirm_password')
        labels = { 'company_name': "Nom de l'entreprise*", 'manager_name': "Nom du propriétaire*", 'profile_photo': "Logo de l'entreprise", 
                  'product': "Type de produits/services*", 'address': "Adresse de l'entreprise*", 
                  'tax_code': "Numéro d'impôt de l'entreprise", 'nrc': "Code NRC de l'entreprise", 
                  'nat_id': "Identité Nationale de l'entreprise", 'email': "Votre email*", 
                  'phone_number': "Votre numéro de téléphone*", 'province': "Province de votre entreprice*"
                  }
        widgets = {'password': forms.PasswordInput, 'confirm_password': forms.PasswordInput}
        print("Azer")
        def clean(self):
            cleaned_data = super().clean()
            password = cleaned_data.get('password')
            confirm_password = cleaned_data.get('confirm_password')

            if password != confirm_password:
                print("erreur mot de passe")
                raise forms.ValidationError("Les mots de passe ne correspondent pas.")
            
            print("ok mot de passe")
            
            required_fields = ['company_name', 'manager_name', 'product', 'province', 'address', 
                               'email', 'phone_number','username', 'password', 'confirm_password']
            for field in required_fields:
                if not cleaned_data.get(field):
                    self.add_error(field, forms.ValidationError("Ce champ est requis"))
        
        def __init__(self, *args, **kwargs):
            super(ProducerRegistrationForm, self).__init__(*args, **kwargs)
            self.fields['sector_label'] = forms.CharField(label='Secteur d activité', max_length=100)
            pass
        # clean(Producer)
        # __init__(Producer)



