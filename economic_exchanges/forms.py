from typing import Any
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

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

class RegisterForm(UserCreationForm):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.fields.pop('password2')
    # username = forms.CharField(max_length=63, label="Nom d'utilisateur")
    # password = forms.CharField(max_length=63, widget=forms.PasswordInput, label="Mot de passe")


