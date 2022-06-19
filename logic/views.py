# from distutils.log import error
from multiprocessing import context
import profile
from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .models import Businesses

@login_required
def home(request):
    context = {}
    return render(request, 'index.html', context=context)


def login_request(request):
    form = LoginForm(request.POST)
    if request.POST:
        if form.is_valid():
            user = form.login(request)
            if user:
                login(request, user)
                return redirect('home')
        else:
            context = {
                'form': form,
                'valid': 'was-validated'
            }
        return render(request, 'auth/login.html', context=context)
    form = LoginForm()
    context = {
        'form': form,
    }
    return render(request, 'auth/login.html', context=context)


def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        print(form.error_messages)
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
        else:
            context = {
                'form': form,
                'valid': 'was-validated'
            }
        return render(request, 'auth/register.html', context=context)

    context = {
        'form': form,
    }
    return render(request, 'auth/register.html', context=context)


def logout_request(request):
    logout(request)
    return redirect('login')


def account(request):
    context={
        "profile":profile
    }
    return render(request, 'account.html' , context=context)
def Business_request(request):
    projects=Businesses.objects.all()
    context={
        "business":projects
    }
    return render(request,'businesses.html', context=context)
