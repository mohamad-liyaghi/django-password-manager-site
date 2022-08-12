from django.urls import  path
from .views import (CreatePassword,
                    PasswordDetail, PasswordUpdate,
                    PasswordDelete, PasswordList)

app_name = "password"

urlpatterns =[
    path("", PasswordList.as_view(), name="home"),
    path('create/',CreatePassword.as_view(),name="add_password"),
    path('detail/<int:id>/<str:token>/',PasswordDetail.as_view(),name="detail"),
    path('update/<int:id>/<str:token>/',PasswordUpdate.as_view(),name="update"),
    path('delete/<int:id>/<str:token>/',PasswordDelete.as_view(),name="delete"),
]