from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import AuthenticationForm

from django import forms
from django.core.exceptions import ValidationError

class RegisterForm(forms.Form):
    first_name = forms.CharField(
        max_length=100, 
        required=True, 
        label="Ad",
        widget=forms.TextInput(attrs={'placeholder': 'Ad', 'class': 'form-control'})
    )
    last_name = forms.CharField(
        max_length=100, 
        required=True, 
        label="Soyad",
        widget=forms.TextInput(attrs={'placeholder': 'Soyad', 'class': 'form-control'})
    )
    email = forms.EmailField(
        required=True, 
        label="E-poçt", 
        widget=forms.EmailInput(attrs={'placeholder': 'E-poçt ünvanı', 'class': 'form-control'})
    )
    phone_number = forms.CharField(
        max_length=14, 
        required=True, 
        label="Telefon nömrəsi",
        widget=forms.TextInput(attrs={'placeholder': 'Telefon nömrəsi', 'class': 'form-control'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Şifrə', 'class': 'form-control'}),
        required=True, 
        label="Şifrə"
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Təkrar şifrə', 'class': 'form-control'}),
        required=True, 
        label="Təkrar şifrə"
    )

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise ValidationError("Şifrələr uyğun gəlmir.")
        return cleaned_data

class LoginForm(forms.Form):
    email = forms.EmailField(
        label="Email", 
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'})
    )
    password = forms.CharField(
        label="Şifrə", 
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Şifrə'})
    )