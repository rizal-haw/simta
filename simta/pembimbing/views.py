from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

class dashboardViewPembimbing(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'pembimbing/index.html')

class pembimbingViewPembimbing(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'pembimbing/pembimbing.html')

class pengajuanJudulViewPembimbing(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'pembimbing/pengajuan-judul.html')

class pengajuanProposalViewPembimbing(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'pembimbing/pengajuan-proposal.html')

class pengajuanTAViewPembimbing(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'pembimbing/pengajuan-ta.html')

class permintaanBimbinganViewPembimbing(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'pembimbing/permintaan-bimbingan.html')

class bimbinganProposalProposalViewPembimbing(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'pembimbing/bimbingan-proposal.html')

class bimbinganTAViewPembimbing(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'pembimbing/bimbingan-ta.html')
