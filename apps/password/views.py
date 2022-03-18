from django.shortcuts import render,redirect, get_object_or_404
from django.views.generic import (
	ListView,
	FormView,
	UpdateView,
	DetailView,
	DeleteView
)
from django.urls import reverse_lazy

from .forms import PassWordForm
from password.models import passwordModel
# Create your views here.
class AllPassword(ListView):
	template_name = "password/list_password.html"
	def get_queryset(self):
		return  passwordModel.objects.filter(owner=self.request.user)
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

class PasswordUpdate(UpdateView):
	template_name =  "password/update_password.html"
	model =  passwordModel
	form_class = PassWordForm
	def get_initial(self):
		return {"password":""}
	def form_valid(self,form):
		owner_form = form.save(commit=False)
		owner_form.owner = self.request.user
		owner_form.password = (__import__('base64').b64encode(owner_form.password.encode()))
		owner_form.save()
		return redirect('account:login')

class PasswordDelete(DeleteView):
	template_name = 'password/delete_password.html'
	model = passwordModel
	success_url = reverse_lazy('account:login')