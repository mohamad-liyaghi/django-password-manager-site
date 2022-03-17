from django.shortcuts import render,redirect
from django.views.generic import (
	ListView,
	FormView,
	UpdateView,
	DeleteView
)
from .forms import PassWordForm
from password.models import passwordModel
# Create your views here.

class CreatePassword(FormView):
	template_name = template_name = "password/add_password.html"
	form_class = PassWordForm
	def form_valid(self,form):
		owner_form = form.save(commit=False)
		owner_form.password = (__import__('base64').b64encode(owner_form.password.encode()))
		owner_form.owner = self.request.user
		owner_form.save()
		return redirect('account:login')
	def form_invalid(self, form):
		print(form.errors)