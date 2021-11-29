from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

def dashboardView(request):
    return render(request, 'tendik/index.html')


def dashboardView(request):
    return render(request, 'tendik/index.html')

def pembimbingView(request):
    return render(request, 'tendik/pembimbing.html')

def mahasiswaView(request):
    return render(request, 'tendik/mahasiswa.html')

def pengajuanJudulView(request):
    return render(request, 'tendik/pengajuanjudul.html')

def proposalView(request):
    return render(request, 'tendik/proposal.html')

def tugasAkhirView(request):
    return render(request, 'tendik/tugas-akhir.html')