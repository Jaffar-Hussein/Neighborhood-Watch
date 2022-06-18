from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.contrib.auth import login, authenticate, logout

def home(request):
    context = {}

    return render(request, 'index.html', context=context)


def login_request(request):
    form = LoginForm()
    if request.method == 'POST':
        if request.method == "POST":
            username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return redirect('login')
    form = LoginForm()
    context = {
        'form': form,
    }
    return render(request, 'auth/login.html', context=context)


def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    context = {
        'form': form,
    }
    return render(request, 'auth/register.html', context=context)

def logout_request(request):
    logout(request)
    return redirect('login')