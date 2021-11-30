from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from . import models

def dashboardViewMhs(request):
    return render(request, 'mhs/index.html')

def pembimbingViewMhs(request):
    return render(request, 'mhs/pembimbing.html')
    

def pengajuanJudulViewMhs(request):
    if request.POST:
        judul_1 = request.POST['judul_1']
        judul_2 = request.POST['judul_2']
        print(judul_1)
        print(judul_2)
        models.Judul.objects.create(
            judul_1=judul_1, judul_2=judul_2)
    data_judul = models.Judul.objects.all()
    return render(request, 'mhs/pengajuan-judul.html', {
        'judul': data_judul
    })

def proposalViewMhs(request):
    return render(request, 'mhs/proposal.html')


def TAViewMhs(request):
    return render(request, 'mhs/tugas-akhir.html')

def seminarproposalViewMhs(request):
    return render(request, 'mhs/seminar-proposal.html')


def sidangskripsiViewMhs(request):
    return render(request, 'mhs/sidang-skripsi.html')
