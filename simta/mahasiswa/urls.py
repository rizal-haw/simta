from django.urls import path
from mahasiswa.views import *
from . import views

urlpatterns = [
    path('', views.dashboardViewMhs, name='index'),
    path('pembimbing', views.pembimbingViewMhs, name='pembimbing'),
    path('pengajuan-judul', views.pengajuanJudulViewMhs, name='pembimbing'),
    path('proposal', views.proposalViewMhs, name='proposal'),
    path('ta', views.TAViewMhs, name='ta'),
    path('seminar-proposal',views.seminarproposalViewMhs, name='seminarproposal'),
    path('sidang-skripsi',views.sidangskripsiViewMhs, name='sidangskripsi'),
    path('buku-panduan',views.bukupanduanViewMhs, name='bukupanduan'),

]