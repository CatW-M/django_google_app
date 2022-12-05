from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from .models import UserProfile

class UserForm(UserCreationForm):
    '''Create variables needed'''
    first_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'placeholder': '*Your first name...'}))
    last_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'placeholder': '*Your last name...'}))
    username = forms.EmailField(max_length=254, required=True, widget=forms.TextInput(attrs={'placeholder': '*Your email...'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': '*Password...','class':'password' }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': '*Confirm Password','class':'password' }))

    #reCAPTCHA token
    token = forms.CharField(widget=forms.HiddenInput())

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2', )

class AuthForm(AuthenticationForm):
    username = forms.EmailField(max_length=254, required=True, widget=forms.TextInput(attrs={'placeholder': '*Email...'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': '*Password...','class':'password' }))

    class Meta:
        model = User
        fields = ('username', 'password',)


class UserProfileForm(forms.ModelForm):

    address = forms.CharField(max_length=100, required=True, widget=forms.HiddenInput())
    city = forms.CharField(max_length=100, required=True, widget=forms.HiddenInput())
    county = forms.CharField(max_length=100, required=True, widget=forms.HiddenInput())
    zip_code = forms.CharField(max_length=10, required=True, widget=forms.HiddenInput())
    country = forms.CharField(max_length=40, required=True, widget=forms.HiddenInput())
    longitude = forms.CharField(max_length=50, required=True, widget=forms.HiddenInput())
    latitude = forms.CharField(max_length=50, required=True, widget=forms.HiddenInput())

    class Meta:
        model = UserProfile
        fields = ('address', 'city', 'county', 'zip_code', 'country', 'longitude', 'latitude')