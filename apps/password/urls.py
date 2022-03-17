from django.urls import  path
from .views import CreatePassword
app_name = "password"
urlpatterns =[
    path('create/',CreatePassword.as_view(),name="add_password")
]