from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import ContactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']

class SignupForm(forms.Form):
    username = forms.CharField(max_length=100, label='Username', widget=forms.TextInput(attrs={'placeholder': 'Enter your username'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'placeholder': 'Enter your email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password'}), label='Password')
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm your password'}), label='Confirm Password')


def clean_username(self):
    username = self.cleaned_data['username']
    
    # Custom validation: Ensure username is not all numeric
    if username.isdigit():
        raise forms.ValidationError("Username cannot be all numeric.")
    # Check if the username already exists
    if User.objects.filter(username=username).exists():
        raise forms.ValidationError("Username already exists.")
    return username
def clean(self):
    cleaned_data = super().clean()
    password = cleaned_data.get("password")
    confirm_password = cleaned_data.get("confirm_password")
    # Check if password and confirm_password match
    if password and confirm_password and password != confirm_password:
        raise forms.ValidationError("Passwords do not match.")
    return cleaned_data




class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Enter your username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password'}))


    def clean_username(self):
        username = self.cleaned_data['username']
        
        # Custom validation: Ensure username is not all numeric
        if username.isdigit():
            raise forms.ValidationError("Username cannot be all numeric.")

        return username