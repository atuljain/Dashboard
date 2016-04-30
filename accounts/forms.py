from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        email = cleaned_data.get("email", "")
        if not User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email address does not exists.")
        return cleaned_data

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({'class': 'form-control', 'required': 'required', 'placeholder': 'Email'})
        self.fields['password'].widget.attrs.update({'class': 'form-control', 'required': 'required', 'placeholder': 'Password'})
