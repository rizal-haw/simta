from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from . import models
from .models import MahasiswaModel
from .forms import MahasiswaForm

def dashboardView(request):
    return render(request, 'tendik/index.html')

def pembimbingView(request):
    return render(request, 'tendik/pembimbing.html')


# -------Operasi Laman Mahasiswa-------------------------

def mahasiswaView(request):
    context ={}

    form = MahasiswaForm(request.POST or None)
    if form.is_valid():
        form.save()
    context['form']= form
    return render(request, 'tendik/mahasiswa.html', context)

def readmahasiswa(request):
    context ={}

    context['tabel_mhs']= MahasiswaModel.objects.all()

    return render(request, 'tendik/mahasiswa.html', context)

def pengajuanJudulView(request):
    return render(request, 'tendik/pengajuanjudul.html')

def proposalView(request):
    return render(request, 'tendik/proposal.html')

def tugasAkhirView(request):
    return render(request, 'tendik/tugas-akhir.html')

def kelolaBimbinganMahasiswaView(request):
    return render(request, 'tendik/kelola-bimbingan-mahasiswa.html')

def kelolaBimbinganDosenView(request):
    return render(request, 'tendik/kelola-bimbingan-dosen.html')