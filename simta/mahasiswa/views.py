from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from . import models
from django.contrib.auth.decorators import login_required
from django.conf import settings
from tendik import models as tendik_models
from tendik.models import PembimbingModel
from pembimbing.models import PenyetujuanJudul

# @login_required(login_url=settings.LOGIN_URL)
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
        judul_ta = request.POST['judul_ta']
        # judul_2 = request.POST['judul_2']
        models.Judul.objects.create(
            judul_ta=judul_ta)
    data_judul = models.Judul.objects.all()
    penyetujuan_judul = PenyetujuanJudul.objects.all()
    return render(request, 'mhs/pengajuan-judul.html', {
        'judul': data_judul,
        'penyetujuan' : penyetujuan_judul
    })

def hapusJudul(request, id):
    models.Judul.objects.filter(pk = id).delete()
    return redirect('/mhs/pengajuan-judul')

# Fungsi disetujui
def penyetujuan(request):
    disetujui = models.PenyetujuanJudul.objects.all()
    konteks = {'data_setuju' : disetujui}
    return render(request, 'mhs/pembimbing.html', konteks)
    
# ----------------------------------------------------
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
    if request.POST:
        nama = request.POST['nama']
        nim = request.POST['nim']
        fakultas = request.POST['fakultas']
        prodi = request.POST['prodi']
        pembimbing_1 = request.POST['pembimbing_1']
        pembimbing_2 = request.POST['pembimbing_2']
        judul = request.POST['judul']
        abstrak = request.POST['abstrak']
        models.sempro.objects.create(
            nama=nama, nim=nim, fakultas=fakultas, prodi=prodi, pembimbing_1=pembimbing_1, pembimbing_2=pembimbing_2, judul=judul, abstrak=abstrak)

    data_sempro = models.sempro.objects.all()
    print (data_sempro)
    return render(request, 'mhs/seminar-proposal.html',{
        'sempro': data_sempro })


def sidangskripsiViewMhs(request):
    return render(request, 'mhs/sidang-skripsi.html')

def bukupanduanViewMhs(request):
    return render(request, 'mhs/buku-panduan.html')

def formulirViewMhs(request):
    return render(request, 'mhs/formulir.html')


