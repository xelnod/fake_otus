from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render


class LoginView(LoginView):
    template_name = 'login.html'


class LogoutView(LogoutView):
    pass
