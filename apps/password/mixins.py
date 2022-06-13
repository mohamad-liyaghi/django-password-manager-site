from  django.shortcuts import  redirect,get_object_or_404
from password.models import  Password

class EditAccess():
    def dispatch(self, request, *args, **kwargs):
        token = self.kwargs.get("token")
        passmodel = get_object_or_404(Password, token= token)
        
        if passmodel.owner == self.request.user:
            return super().dispatch(request, *args, **kwargs)
        else:
            return redirect("password:home")