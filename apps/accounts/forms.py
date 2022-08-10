from django import  forms
from  django.contrib.auth.forms import UserCreationForm
from accounts.models import User

class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('nick_name', 'email', 'token', 'password')
        help_texts = {
            'password' : None,
        }
