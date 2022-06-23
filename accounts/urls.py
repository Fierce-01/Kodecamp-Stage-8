from django.urls import path
from .views import Signup
from django.contrib.auth import views as auth_views

app_name='accounts'

urlpatterns = [
    path('signup/', Signup, name='signupview'),
    path('signin/', auth_views.LoginView.as_view(template_name='accounts/signin.html'), name='signinview'),
    path('logout/', auth_views.LogoutView.as_view(template_name='accounts/logout.html'), name='logoutview'),
]