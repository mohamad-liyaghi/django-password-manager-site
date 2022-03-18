from django.urls import  path
from .views import (CreatePassword,
                    PasswordDetail,
                    PasswordUpdate,
                    PasswordDelete,
                    AllPassword)
app_name = "password"
urlpatterns =[
    path("",AllPassword.as_view(),name="home"),
    path('create/',CreatePassword.as_view(),name="add_password"),
    path('detail/<int:pk>/',PasswordDetail.as_view(),name="detail"),
    path('update/<int:pk>/',PasswordUpdate.as_view(),name="update"),
    path('delete/<int:pk>/',PasswordDelete.as_view(),name="delete"),
]