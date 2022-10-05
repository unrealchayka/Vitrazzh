from django import forms
from django.core.validators import RegexValidator



class TelegramMessageForm(forms.Form):
    phoneNumberRegex = RegexValidator(regex = r"^\+?1?\d{8,15}$")
    name = forms.CharField(max_length=30)
    phone = forms.CharField(max_length=12, validators=[phoneNumberRegex])
