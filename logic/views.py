from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm, PostsForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .models import Businesses, Neighbourhood, Profile, Posts


@login_required
def home(request):
    current_user = request.user
    neighbour=Profile.objects.get(user=current_user)
    business = Businesses.objects.all().filter(neighbourhood=neighbour.neighbourhood)[0:3]
    posts  = Posts.objects.all().filter(neighbourhood=neighbour.neighbourhood)
    user = Profile.objects.filter(user=request.user).first()
    neighbourhood = Neighbourhood.objects.filter(occupants=Profile.objects.get(user=request.user)).first()
    context = {
        "business": business,
        "posts": posts,
        "user": user,
        "neighbourhood": neighbourhood
    }

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
    current_user = Profile.objects.filter(user=request.user)
    user = Profile.objects.filter(user=request.user).first()
    neigbourhood = Neighbourhood.objects.all()
    posts = Posts.objects.filter(writer=Profile.objects.get(user=request.user))
    if request.method == 'POST':
        data = request.POST.get('q')
        if data:
            current_user.update(
                neighbourhood=Neighbourhood.objects.get(id=data))
            return redirect('account')
        # print(request.POST.data)

    context = {
        "profile": current_user.first(),
        "neigbourhoods": neigbourhood,
        "posts": posts,
        "user": user
    }
    return render(request, 'account.html', context=context)


def Business_request(request):
    projects = Businesses.objects.all()
    user = Profile.objects.filter(user=request.user).first()
    
    context = {
        "business": projects,
        "user": user
    }
    return render(request, 'businesses.html', context=context)


def post_request(request):
    form = PostsForm
    if request.method == 'POST':
        form = PostsForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            image = form.cleaned_data['image']
            neighbour=Profile.objects.get(user=request.user)
            neighbourhood=neighbour.neighbourhood
            form = Posts.objects.create(title=title, content=content,neighbourhood=neighbourhood,
                             writer=Profile.objects.get(user=request.user),image=image)
            form.save()
            return redirect('home')
    context = {
        'form': form
    }
    return render(request, 'post.html', context=context)
