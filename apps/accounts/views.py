from django.shortcuts import render,redirect
from django.contrib.auth.views import LoginView
from django.views.generic import  CreateView
from django.urls import reverse_lazy
from .forms import  RegisterForm
from django.contrib.auth import logout


def logout_user(request):
	logout(request)
	return redirect('password:home')