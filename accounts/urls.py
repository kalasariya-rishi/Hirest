from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('register', register_attempt, name="register_attempt"),
    path('accounts/login/', login_attempt, name="login_attempt"),
    path('token', token_send, name="token_send"),
    path('success', success, name='success'),
    path('error', error_page, name="error"),
    path('signout', signout, name='signout'),
    path('change-password/<token>/', change_password, name="change-password"),
    path('forget-password/', forget_password, name='forget-password'),
    # path('forget-password/', forget, name='forget-password'),
]
