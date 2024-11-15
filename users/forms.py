from typing import Any
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import profileModel

class signUpForm(UserCreationForm):
    email = forms.EmailField()
    class Meta():
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super(signUpForm, self).__init__(*args, **kwargs)

        for fieldname in ('username', 'email', 'password1', 'password2'):
            self.fields[fieldname].help_text = None

class updateUser(forms.ModelForm):
    class Meta():
        model = User
        fields = ('username', 'email',)


class updateProfile(forms.ModelForm):
    class Meta():
        model = profileModel
        fields = ('image',)