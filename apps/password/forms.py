from django import  forms
from password.models import  passwordModel
class PassWordForm(forms.ModelForm):
    class Meta:
        model = passwordModel
        fields = "__all__"
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your title'}),
            'password': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter your password'}),
        }

