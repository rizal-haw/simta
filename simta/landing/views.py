from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

class Index(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'landing/index.html')

def login_user(request):
    return render(request, 'authenticate/login.html')