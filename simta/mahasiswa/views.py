from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

def dashboardViewMhs(request):
    return render(request, 'mhs/index.html')

def pembimbingViewMhs(request):
    return render(request, 'mhs/pembimbing.html')

def pengajuanJudulViewMhs(request):
    return render(request, 'mhs/pengajuan-judul.html')

def proposalViewMhs(request):
    return render(request, 'mhs/proposal.html')

def TAViewMhs(request):
    return render(request, 'mhs/tugas-akhir.html')

