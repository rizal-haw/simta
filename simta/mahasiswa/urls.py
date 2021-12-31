from django.urls import path
from mahasiswa.views import *
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('pembimbing', views.pembimbingViewMhs, name='pembimbing'),
    path('pengajuan-judul/', views.pengajuanJudulViewMhs, name='pengajuan-judul'),
    path('hapus-judul/<id>', views.hapusJudul, name='hapus-judul'),
    path('hapus-pembimbing/<id>', views.hapusPembimbing, name='hapus-pembimbing'),
    path('proposal', views.proposalViewMhs, name='proposal'),
    path('ta', views.TAViewMhs, name='ta'),
    path('seminar-proposal',views.seminarproposalViewMhs, name='seminar-proposal'),
    path('sidang-skripsi',views.sidangskripsiViewMhs, name='sidang-skripsi'),
    path('buku-panduan',views.bukupanduanViewMhs, name='buku-panduan'),
    path('formulir',views.formulirViewMhs, name='formulir'),
]