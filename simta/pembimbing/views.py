from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

def dashboardViewPembimbing(request):
    return render(request, 'pembimbing/index.html')

def pembimbingViewPembimbing(request):
    return render(request, 'pembimbing/pembimbing.html')

def pengajuanJudulViewPembimbing(request):
    return render(request, 'pembimbing/pengajuan-judul.html')

def pengajuanProposalViewPembimbing(request):
    return render(request, 'pembimbing/pengajuan-proposal.html')

def pengajuanTAViewPembimbing(request):
    return render(request, 'pembimbing/pengajuan-ta.html')

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
