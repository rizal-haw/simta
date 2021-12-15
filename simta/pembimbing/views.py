from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from . import models

def dashboardViewPembimbing(request):
    return render(request, 'pembimbing/index.html')

def pembimbingViewPembimbing(request):
    return render(request, 'pembimbing/pembimbing.html')

# ---------------Halaman Pengajuan Judul-----------------

def pengajuanJudulViewPembimbing(request):
    data_judul = models.Judul.objects.all()
    konteks = {'data_judul': data_judul}
    return render(request, 'pembimbing/pengajuan-judul.html', konteks)
# -------end----------------------------------------------

# -------Halaman Pengajuan Proposal------------------------

def pengajuanProposalViewPembimbing(request):
    data_proposal = models.proposal.objects.all()
    konteks = {'data_proposal': data_proposal}
    return render(request, 'pembimbing/pengajuan-proposal.html', konteks)
# --------End-----------------------------------------------

def pengajuanTAViewPembimbing(request):
    data_ta = models.ta.objects.all()
    konteks = {'data_ta': data_ta}
    return render(request, 'pembimbing/pengajuan-ta.html',konteks)

def permintaanBimbinganViewPembimbing(request):
    return render(request, 'pembimbing/permintaan-bimbingan.html')

def bimbinganProposalProposalViewPembimbing(request):
    return render(request, 'pembimbing/bimbingan-proposal.html')

def bimbinganTAViewPembimbing(request):
    return render(request, 'pembimbing/bimbingan-ta.html')

def jadwalTAViewPembimbing(request):
    return render(request, 'pembimbing/jadwal.html')

def panduanTAViewPembimbing(request):
    return render(request, 'pembimbing/panduan.html')
