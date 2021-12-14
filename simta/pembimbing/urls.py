from django.urls import path
from pembimbing.views import *
from . import views

urlpatterns = [
    path('', views.dashboardViewPembimbing, name='index'),
    path('pembimbing', views.pembimbingViewPembimbing, name='pembimbing'),
    # Laman Pengajuan Judul
    path('pengajuan-judul', views.pengajuanJudulViewPembimbing, name='pengajuan-judul'),
    path('detail-judul/<id>', views.detailJudul, name='detail-judul '),
    # ---
    path('pengajuan-proposal', views.pengajuanProposalViewPembimbing, name='pengajuan-propposal'),
    path('pengajuan-ta', views.pengajuanTAViewPembimbing, name='pengajuan-ta'),
    path('permintaan-bimbingan', views.permintaanBimbinganViewPembimbing, name='Permintaan-bimbingan'),
    path('bimbingan-proposal', views.bimbinganProposalProposalViewPembimbing, name='bimbingan-proposal'),
    path('bimbingan-ta', views.bimbinganTAViewPembimbing, name='bimbingan-ta'),
    path('jadwal', views.jadwalTAViewPembimbing, name='jadwal'),
    path('panduan', views.panduanTAViewPembimbing, name='panduan'),
]