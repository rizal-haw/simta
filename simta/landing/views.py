from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import SignUpForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def index(request):
    return render(request, 'landing/index.html')

def register(request):
    msg = None
    if request.method=='POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'user created'
            return redirect('login')
        else:
            msg = 'Form is Invalid'
    else:
        form = SignUpForm()
 
    return render(request, 'authenticate/register.html', {'form' : form, 'msg' : msg})

def login_user(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_tendik:
                login (request, user)
                return redirect('/tendik/')
            elif user is not None and user.is_mhs:
                login (request, user)
                return redirect('/mhs/')
            elif user is not None and user.is_pembimbing:
                login (request, user)
                return redirect('/pembimbing/')
            else:
                msg = 'invalid data'
        else:
            msg = 'error validating data'
        
    return render(request, 'authenticate/login.html', {'form' : form, 'msg' : msg})

def logout_user(request):
    logout(request)
    return redirect('/')
