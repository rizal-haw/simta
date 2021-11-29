from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from . import models

def dashboardView(request):
    return render(request, 'tendik/index.html')

def pembimbingView(request):
    return render(request, 'tendik/pembimbing.html')

def mahasiswaView(request):
    if request.POST:
        nama = request.POST['nama']
        nim = request.POST['nim']
        prodi = request.POST['prodi']
        fakultas = request.POST['fakultas']
        kelas = request.POST['kelas']
        semester = request.POST['semester']
        models.Mahasiswa.objects.all()
    return render(request, 'tendik/mahasiswa.html')

def pengajuanJudulView(request):
    return render(request, 'tendik/pengajuanjudul.html')

def proposalView(request):
    return render(request, 'tendik/proposal.html')

def tugasAkhirView(request):
    return render(request, 'tendik/tugas-akhir.html')