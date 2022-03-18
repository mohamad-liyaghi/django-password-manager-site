from  django.shortcuts import  redirect,get_object_or_404
from password.models import  passwordModel

class EditAccess():
    def dispatch(self, request, pk, *args, **kwargs):
        passmodel = get_object_or_404(passwordModel, pk=pk)
        if passmodel.owner == self.request.user:
            return super().dispatch(request, *args, **kwargs)
        else:
            return redirect("password:home")