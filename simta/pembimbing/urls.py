from django.urls import path
from pembimbing.views import *

urlpatterns = [
    path('', dashboardViewPembimbing.as_view(), name='index'),
    path('pembimbing', pembimbingViewPembimbing.as_view(), name='pembimbing'),
    path('pengajuan-judul', pengajuanJudulViewPembimbing.as_view(), name='pembimbing'),
    path('pengajuan-proposal', pengajuanProposalViewPembimbing.as_view(), name='pembimbing'),
]