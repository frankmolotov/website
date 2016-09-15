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
        self.fields['user_name'].widget = TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Name und Vorname *', 'id': 'inputSuccess2'})
        self.fields['email'].widget = TextInput(
            attrs={'class': 'form-control', 'placeholder': 'E-Mail *', 'id': 'inputSuccess2'})
        self.fields['phone_number'].widget = TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Telefonnummer *', 'data-country': 'DE',
                   'id': 'inputSuccess2'})
        # for field in self.fields.values():
        #   field.error_messages = {'required': 'Pole {fieldname} is required'.format(fieldname=field.label)}


    class Meta:
        model = Register
        fields = {'user_name', 'email', 'phone_number'}
