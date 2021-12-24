from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from . import models
from tendik import models as tendik_models
from tendik.models import PembimbingModel

def dashboardViewMhs(request):
    return render(request, 'mhs/index.html')

# ---------------------Halaman Pembibmbing-------------------------------------


def pembimbingViewMhs(request):
    if request.POST:

        pembimbing_1 = request.POST['pembimbing_1']
        pembimbing_2 = request.POST['pembimbing_2']
        models.pembimbing.objects.create(
            pembimbing_1 = pembimbing_1, pembimbing_2 = pembimbing_2,)
        print(pembimbing_1)
        print(pembimbing_2)
    data_pembimbing =  PembimbingModel.objects.all()
    print(data_pembimbing)
    return render(request, 'mhs/pembimbing.html', {
        'pembimbing': data_pembimbing
    })

# End Halaman Pembimbing----------------------------------------------

# ----------------------------Halaman Pengajuan Judul----------------- 

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

def hapusJudul(request, id):
    models.Judul.objects.filter(pk = id).delete()
    return redirect('mhs/pengajuan-judul')
    

def proposalViewMhs(request):
    if request.POST:
        nama = request.POST['nama']
        nim = request.POST['nim']
        judul = request.POST['judul']
        pembimbing_1 = request.POST['pembimbing_1']
        pembimbing_2 = request.POST['pembimbing_2']
        models.proposal.objects.create(
         nama = nama, nim = nim, judul= judul, pembimbing_1 = pembimbing_1, pembimbing_2 = pembimbing_2)
         
    data_proposal = models.proposal.objects.all()
    print(data_proposal)
    return render(request, 'mhs/proposal.html',{
    'proposal': data_proposal })

# -------------------------------------------------------

# ----------------------Halaman TA-----------------------

def TAViewMhs(request):
    if request.POST:
        nim = request.POST['nim']
        nama = request.POST['nama']
        judul = request.POST['judul']
        pembimbing_1 = request.POST['pembimbing_1']
        pembimbing_2 = request.POST['pembimbing_2']
        models.ta.objects.create(
         nama = nama, nim = nim, judul= judul, pembimbing_1 = pembimbing_1, pembimbing_2 = pembimbing_2)
         
    data_ta = models.ta.objects.all()
    print(data_ta)
    return render(request, 'mhs/tugas-akhir.html', {
    'ta': data_ta })

def seminarproposalViewMhs(request):
    return render(request, 'mhs/seminar-proposal.html')


def sidangskripsiViewMhs(request):
    return render(request, 'mhs/sidang-skripsi.html')

def bukupanduanViewMhs(request):
    return render(request, 'mhs/buku-panduan.html')

def formulirViewMhs(request):
    return render(request, 'mhs/formulir.html')


