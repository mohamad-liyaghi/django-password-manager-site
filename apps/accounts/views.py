from django.shortcuts import render,redirect
from django.contrib.auth.views import LoginView
from django.views.generic import  CreateView
from django.urls import reverse_lazy
from .forms import  RegisterForm
from django.contrib.auth import logout

class Register_user(CreateView):
    form_class = RegisterForm
    template_name = 'accounts/register.html'
    def form_valid(self, form):
        form.save()
        return  redirect('password:home')
    def form_invalid(self, form):
        print(form.error)
def logout_user(request):
	logout(request)
	return redirect('password:home')