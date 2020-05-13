from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.myAccount, name='MyAccountPage'),
    path('signup', views.handleSignUp, name='SignUpPage'),
    path('signin', views.handleSignin, name='SigninPage'),
    path('logout', views.handleLogout, name='LogoutPage'),
    path('@<str:username>', views.userProfile, name='UserProfilePage'),
]