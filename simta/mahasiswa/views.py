from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

class dashboardViewMhs(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'mhs/index.html')

class pembimbingViewMhs(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'mhs/pembimbing.html')

class pengajuanJudulViewMhs(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'mhs/pengajuan-judul.html')

