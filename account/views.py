from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect

import random

from django.core.mail import send_mail
from django.conf import settings


from account.models import *

def login_page(request):
    if request.method == 'POST':
        name = request.POST['name']
        password = request.POST['password']
        user = authenticate(username=name, password=password)
        if user:
            prof = work.objects.get(user=user)
            if prof.is_verified == True :
                login(request, user)
                return redirect('products')
        else:
            messages.error(request, 'Your Username or Password is Incorrect')
            return redirect('login')
    return render(request, 'Accounts/login.html')


def registration_page(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']
        if password == password1:
            if User.objects.filter(username=name).exists():
                messages.info(request, 'Username Already Exists , Choose Another one')
                return redirect('reg')
            else:
                user = User.objects.create_user(username=name, email=email, password=password)
                user.set_password(password)
                user.save()
                otp = random.randint(0000, 9999)
                prof = work(user=user,token= otp)
                prof.save()
                print(otp)
                subject = "your Account Verification OTP"
                message = f'hi this is verufy otp {otp}'
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [email]
                send_mail(subject, message, email_from, recipient_list)
                messages.success(request, 'Account created to verify check your mail.')
                print(otp)
                return redirect('verify_acc')
        else:
            messages.error(request, 'Please Make Password Same')
            return redirect('reg')
    return render(request, 'Accounts/login.html')


def log_out(request):
    logout(request)
    messages.success(request, 'Log out Success')
    return redirect('login')

def forget_pass(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['new_pass']
        if name != None:
            user = User.objects.get(username=name)
            print(user)
            print(user.email)
            if user.email == email:
                user.set_password(password)
                user.save()
                update_session_auth_hash(request, user)
                messages.success(request, 'password change done')
                return redirect('login')
            else:
                messages.error(request, 'email not matched')

    return render(request, 'Accounts/forget_pass.html')

def verify_acc(request):
    if request.method == 'POST':
        otp = request.POST.get('otp')
        print(otp)
        try:
            prof = work.objects.get(token=otp)
            print(prof)
            prof.is_verified = True
            prof.save()
            messages.success(request, "Profile successfully verified!")
            return redirect('login')
        except:
            messages.error(request,"Wrong otp!")
            return redirect('verify_acc')

    return render(request, 'Accounts/verify.html')