from django.urls import path
from pembimbing.views import *

urlpatterns = [
    path('', dashboardViewPembimbing.as_view(), name='index'),
    path('pembimbing', pembimbingViewPembimbing.as_view(), name='pembimbing'),
    path('pengajuan-judul', pengajuanJudulViewPembimbing.as_view(), name='pembimbing'),
    path('pengajuan-proposal', pengajuanProposalViewPembimbing.as_view(), name='pengajuan-propposal'),
    path('pengajuan-ta', pengajuanTAViewPembimbing.as_view(), name='pengajuan-ta'),
    path('permintaan-bimbingan', permintaanBimbinganViewPembimbing.as_view(), name='Permintaan-bimbingan'),
    path('bimbingan-proposal', bimbinganProposalProposalViewPembimbing.as_view(), name='bimbingan-proposal'),
    path('bimbingan-ta', bimbinganTAViewPembimbing.as_view(), name='bimbingan-ta'),
]