from django import  forms
from password.models import  Password
class PassWordForm(forms.ModelForm):
    class Meta:
        model = Password
        fields = ("title", "password", "owner", "token")
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your title'}),
            'password': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter your password'}),
        }

