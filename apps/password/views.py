from django.shortcuts import redirect, get_object_or_404

from django.views.generic import (
	ListView, FormView, UpdateView,
	DetailView, DeleteView
)

from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
import uuid 

from .forms import PassWordForm
from .encryption import decode, encode
from .mixins import EditAccess
from password.models import Password

# Create your views here.

class PasswordList(LoginRequiredMixin,ListView):
	'''
		Main Page
	'''
	template_name = "password/list_password.html"
	def get_queryset(self):
		return  Password.objects.filter(owner=self.request.user)
		
class CreatePassword(LoginRequiredMixin, FormView):
	'''
		Save a password and encode it to base64
	'''
	template_name = template_name = "password/add_password.html"
	form_class = PassWordForm

	def form_valid(self,form):
		form = form.save(commit=False)
		form.password = encode(form.password)
		form.token =  uuid.uuid4().hex.upper()[0:15]
		form.owner = self.request.user
		form.save()
		return redirect('password:home')

class PasswordDetail(LoginRequiredMixin, EditAccess, DetailView):
	'''
		Detail page for password
	'''
	template_name = "password/detail_password.html"

	def get_object(self):
		token = self.kwargs.get('token')
		id = self.kwargs.get("id")
		object = get_object_or_404(Password, id= id, token= token)
		global password_context
		password_context = decode(object.password)
		return object

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['password'] = str(password_context).replace('b','').replace("'","")
		return context


class PasswordUpdate(LoginRequiredMixin,UpdateView,EditAccess):
	template_name =  "password/update_password.html"
	model =  Password
	fields = ["title","password"]
	pk_url_kwarg = 'token'

	def get_initial(self):
		return {"password":""}

	def get_object(self):
		return get_object_or_404(Password, id= self.kwargs["id"], token= self.kwargs["token"])

	def form_valid(self,form):
		owner_form = form.save(commit=False)
		owner_form.password = (__import__('base64').b64encode(owner_form.password.encode()))
		owner_form.save()
		return redirect('password:home')

class PasswordDelete(LoginRequiredMixin, EditAccess, DeleteView):
	template_name = 'password/delete_password.html'
	pk_url_kwarg = 'token'
	model = Password
	success_url = reverse_lazy('password:home')

	def get_object(self):
		return get_object_or_404(Password, id= self.kwargs["id"], token= self.kwargs["token"])