from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Comment, Car


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['company', 'name', 'year', 'image', 'description', 'engine_type', 'body_type', 'horsepower', 'price']


class VehicleFilterForm(forms.Form):
    BODY_TYPE_CHOICES = [
        ('sedan', 'Sedan'),
        ('suv', 'SUV'),
        ('supercar', 'Supercar'),
        ('pickup', 'Pickup'),
        ('hatchback', 'Hatchback'),
        ('convertible', 'Convertible'),
        ('minivan', 'Minivan'),
        ('coupe', 'Coupe'),
        ('sportscar', 'Sports car'),
        ('fastback', 'Fastback')
    ]
    body_type = forms.ChoiceField(choices=BODY_TYPE_CHOICES, required=False, label='Body Type')


class SendForm(forms.Form):
    user_mail = forms.EmailField()
