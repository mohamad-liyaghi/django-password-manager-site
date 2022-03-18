from django.urls import path
from .views import Login_user,Register_user,logout_user
app_name = "account"
urlpatterns = [
    path("login/",Login_user.as_view(),name="login"),
    path('register/',Register_user.as_view(),name="register"),
    path('logout/',logout_user,name="logout")
]