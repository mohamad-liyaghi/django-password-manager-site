from django.shortcuts import render,redirect, get_object_or_404
from django.views.generic import (
	ListView,
	FormView,
	UpdateView,
	DetailView,
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

class PasswordDetail(DetailView):
	template_name = "password/detail_password.html"
	def get_object(self):
		pk = self.kwargs.get('pk')
		object = get_object_or_404(passwordModel,pk=pk)
		global password_context
		password_context = str((__import__('base64').b64decode(object.password.replace("b",""))))
		return object

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['password'] = password_context.replace("b","")
		return context