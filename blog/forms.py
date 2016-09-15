from django import forms
from .models import Register, Count
from .fields import ReCaptchaField
from django.forms.widgets import TextInput, EmailInput
from django.forms import widgets


class RegisterForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['user_name'].required = False
        self.fields['email'].required = False
        self.fields['phone_number'].required = False
        self.fields['count_of_users'].required = False
        self.fields['user_name'].widget = TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Name und Vorname *', 'id': 'inputSuccess2',
                   'data-required': "Bitte geben Sie Ihre Namen ein"})
        self.fields['email'].widget = TextInput(
            attrs={'class': 'form-control', 'placeholder': 'E-Mail *', 'id': 'inputSuccess2',
                   'data-required': "Bitte geben Sie Ihre E-mail ein"})
        self.fields['phone_number'].widget = TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Telefonnummer *', 'data-country': 'DE',
                   'id': 'inputSuccess2', 'data-required': "Bitte geben Sie Ihre Telefonnummer ein"})


    class Meta:
        model = Register
        fields = {'user_name', 'email', 'phone_number','count_of_users'}

'''class CountForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(CountForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Count
        fields = {'count_of_users', 'capital'}'''
