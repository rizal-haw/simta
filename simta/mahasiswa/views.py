from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from . import models

def dashboardViewMhs(request):
    return render(request, 'mhs/index.html')

def pembimbingViewMhs(request):
    if request.POST:

        pembimbing_1 = request.POST['pembimbing_1']
        pembimbing_2 = request.POST['pembimbing_2']
        models.pembimbing.objects.create(
            pembimbing_1 = pembimbing_1, pembimbing_2 = pembimbing_2,)
        print(pembimbing_1)
        print(pembimbing_2)
    data_pembimbing =  models.pembimbing.objects.all()
    return render(request, 'mhs/pembimbing.html', {
        'pembimbing': data_pembimbing
    })
    

def pengajuanJudulViewMhs(request):
    if request.POST:
        judul_1 = request.POST['judul_1']
        judul_2 = request.POST['judul_2']
        models.Judul.objects.create(
            judul_1=judul_1, judul_2=judul_2)
    data_judul = models.Judul.objects.all()
    print(data_judul)
    return render(request, 'mhs/pengajuan-judul.html', {
        'judul': data_judul
    })

def proposalViewMhs(request):
    if request.POST:
        nama = request.POST['nama']
        nim = request.POST['nim']
        judul = request.POST['judul']
        pembimbing_1 = request.POST['pembimbing_1']
        pembimbing_2 = request.POST['pembimbing_1']
        models.proposal.objects.create(
         nama = nama, nim = nim, judul= judul, pembimbing_1 = pembimbing_1, pembimbing_2 = pembimbing_2)
         
    data_proposal = models.proposal.objects.all()
    print(data_proposal)
    return render(request, 'mhs/proposal.html',{
    'proposal': data_proposal })

def TAViewMhs(request):
    return render(request, 'mhs/tugas-akhir.html')

def seminarproposalViewMhs(request):
    return render(request, 'mhs/seminar-proposal.html')


def sidangskripsiViewMhs(request):
    return render(request, 'mhs/sidang-skripsi.html')

def bukupanduanViewMhs(request):
    return render(request, 'mhs/buku-panduan.html')

def formulirViewMhs(request):
    return render(request, 'mhs/formulir.html')


