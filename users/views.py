from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.contrib.auth.models import User

from django.contrib import messages


# Create your views here.
def profiles(request):
    return render(request, 'users/profiles.html')

def loginUser(request):

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
            return redirect('profiles')
        else:
            messages.error(request, 'Username OR password is incorrect')
            # print('Username OR password is incorrect')
    return render(request, 'users/login_register.html')

def registerUser(request):
    return render(request, 'users/register_user.html')

def logoutUser(request):
    logout(request)
    return redirect('index')