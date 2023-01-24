import email

from accounts.models import Profile
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from .models import *
from django.http import HttpResponse
import uuid
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# from .helpers import send_forget_password_mail
import uuid
# send_mail_app.tasks if change

# from django.core.mail import send_mail
import uuid
from django.conf import settings
from .tasks import *


# Create your views here.

@login_required
def home(request):
    return render(request, 'home.html')


def login_attempt(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user_obj = User.objects.filter(username=username).first()
        if user_obj is None:
            messages.success(request, 'User not found.')
            return redirect('/accounts/login')

        profile_obj = Profile.objects.filter(user=user_obj).first()

        user = authenticate(username=username, password=password)
        if user is None:
            messages.success(request, 'Wrong password.')
            return redirect('/accounts/login')

        login(request, user)
        return redirect('/')

    return render(request, 'login.html')


def register_attempt(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(password)
        print(email)

        try:
            if User.objects.filter(username=username).first():
                messages.success(request, 'Username is taken.')
                return redirect('/register')

            if User.objects.filter(email=email).first():
                messages.success(request, 'Email is taken.')
                return redirect('/register')

            user_obj = User(username=username, email=email)
            user_obj.set_password(password)
            user_obj.save()
            auth_token = str(uuid.uuid4())
            print(auth_token)
            profile_obj = Profile.objects.create(user=user_obj, auth_token=auth_token, email=email)
            profile_obj.save()
            print(auth_token)
            print(user_obj.username)

            return redirect('/accounts/login')

        except Exception as e:
            print(e)

    return render(request, 'register.html')


def auth_t(auth_token):
    token = auth_token


def success(request):
    return render(request, 'success.html')


def token_send(request):
    return render(request, 'token_send.html')


def error_page(request):
    return render(request, 'error.html')





def send_mail_after_registration(email, token):
    subject = 'Your accounts need to be verified'
    message = f'Hi paste the link to verify your account http://127.0.0.1:8000/verify/{token}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, email_from, recipient_list)


def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully!!")
    return redirect('/')


# def forget(request):
#     return render(request, 'forget-password.html')


# def change(request):
#     return render(request, 'change-password.html')


def change_password(request, token):
    return render(request, 'change-password.html')


def forget_password(request):
    return render(request, 'forget-password.html')

# subject = "Your forget password link" message = f'Hi, click one the link to reset your password
# http://127.0.0.1:8000/http://127.0.0.1:8000/change-password/{token}/ ' email_from = settings.EMAIL_HOST_USER
# recipient_list = [email1] send_mail(subject, message, email_from, recipient_list) return True
