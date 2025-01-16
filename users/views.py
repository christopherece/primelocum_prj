from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.contrib.auth.models import User

from django.contrib import messages
from .forms import CustomUserCreationForm

# Create your views here.
@login_required(login_url='login')
def profiles(request):
    return render(request, 'users/profiles.html')

def loginUser(request):

    page = 'login'
    if request.user.is_authenticated:
        return redirect('profiles')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Username does not exist')
            # print('Username does not exist')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('account')
        else:
            messages.error(request, 'Username OR password is incorrect')
            # print('Username OR password is incorrect')
    return render(request, 'users/login_register.html')

def registerUser(request):
    page = 'register'
    form = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'User account was created!')
            login(request, user)
            return redirect('account')
        else:
            messages.error(request, 'An error has occurred during registration')
    context = {'page': page, 'form': form }
    return render(request, 'users/login_register.html',context)

def logoutUser(request):
    logout(request)
    messages.info(request, 'User was logged out!')
    return redirect('index')

@login_required(login_url='login')
def userAccount(request):
    profile = request.user.profile
    context = {'profile': profile}
    return render(request, 'users/account.html', context)
