from django.urls import  path
from .views import CreatePassword,PasswordDetail
app_name = "password"
urlpatterns =[
    path('create/',CreatePassword.as_view(),name="add_password"),
    path('detail/<int:pk>/',PasswordDetail.as_view(),name="update")
]