from django import forms
from .models import NewUser
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    is_hospital = forms.BooleanField(required=False)

    class Meta:
        model = NewUser
        fields = ['user_name', 'email', 'is_hospital', 'password1', 'password2']

        