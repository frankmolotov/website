from django import forms
from .models import Post, Register
from .fields import ReCaptchaField

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text')


class RegisterForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['email'].required = True
        self.fields['first_name'].required = True
        self.fields['phone_number'].required = True

    class Meta:
        model = Register
        recaptcha = ReCaptchaField()
        fields = {'first_name', 'last_name', 'email', 'phone_number'}

