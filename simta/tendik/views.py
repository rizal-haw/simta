from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
class dashboardView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'tendik/index.html')

class pembimbingView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'tendik/pembimbing.html')