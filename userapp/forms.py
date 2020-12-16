from django import forms
from .models.user_model import Register

class RegisterForm(forms.Form):
    username = forms.CharField(required=True)
    email = forms.CharField((required=True))
    password = forms.CharField((required=True))