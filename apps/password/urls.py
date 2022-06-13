from django.urls import  path
from .views import (CreatePassword,
                    PasswordDetail, PasswordUpdate,
                    PasswordDelete, PasswordList)


urlpatterns =[
    path("", PasswordList.as_view(), name="home"),
    path('create/',CreatePassword.as_view(),name="add_password"),
    path('detail/<str:token>/',PasswordDetail.as_view(),name="detail"),
    path('update/<str:token>/',PasswordUpdate.as_view(),name="update"),
    path('delete/<str:token>/',PasswordDelete.as_view(),name="delete"),
]