from django import  forms
from  django.contrib.auth.forms import UserCreationForm

import random

from accounts.models import User

class RegisterForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('nick_name', 'email', 'password')
        help_texts = {
            'password' : None,
        }

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.token = random.randint(1, 99999999999999)

        if commit:
            user.save()

        return user
