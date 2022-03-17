from django.shortcuts import render,redirect
from django.contrib.auth.views import LoginView
from django.views.generic import  CreateView
from django.urls import reverse_lazy
from .forms import  RegisterForm

# Create your views here.
class Login_user(LoginView):
    template_name = "account/login.html"
    def get_success_url(self):
        return reverse_lazy("account:login")

class Register_user(CreateView):
    form_class = RegisterForm
    template_name = 'account/register.html'
    def form_valid(self, form):
        form.save()
        return  redirect("account:register")