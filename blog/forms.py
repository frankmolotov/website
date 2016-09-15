from django import forms
from .models import Post, Register
from .fields import ReCaptchaField
from django.forms.widgets import TextInput, EmailInput
from django.forms import widgets


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text')


class RegisterForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['email'].error_messages = {'required': 'Bitte geben Sie Ihre E-mail ein'}
        self.fields['user_name'].error_messages = {'required': 'Bitte geben Sie Ihre Namen ein'}
        self.fields['phone_number'].error_messages = {'required': 'Bitte geben Sie Ihre Telefonnummer ein'}
        self.fields['user_name'].widget = TextInput(
            attrs={'type': 'name', 'class': 'form-control', 'placeholder': 'Name und Vorname *', 'id': 'inputSuccess2',
                   'required': ''})
        self.fields['email'].widget = TextInput(
            attrs={'type': 'email', 'class': 'form-control', 'placeholder': 'E-Mail *', 'id': 'inputSuccess2',
                   'required': 'required'})
        self.fields['phone_number'].widget = TextInput(
            attrs={'type': 'tel', 'class': 'form-control', 'placeholder': 'Telefonnummer *', 'data-country': 'DE',
                   'id': 'inputSuccess2', 'required': 'required'})
        # for field in self.fields.values():
        #   field.error_messages = {'required': 'Pole {fieldname} is required'.format(fieldname=field.label)}

    class Meta:
        model = Register
        fields = {'user_name', 'email', 'phone_number'}
