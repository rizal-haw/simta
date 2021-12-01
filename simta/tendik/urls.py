from django.urls import path
from tendik.views import *
from . import views

urlpatterns = [
    path('', views.dashboardView, name='index'),
    path('pembimbing', views.pembimbingView, name='pembimbing'),
    path('mahasiswa', views.mahasiswaView, name='mahasiswa'),
    path('pengajuan-judul', views.pengajuanJudulView, name='pengajuan-judl'),
    path('proposal', views.proposalView, name='proposal'),
    path('tugas-akhir', views.tugasAkhirView, name='tugas-akhir'),
    path('kelola-bimbingan-mahasiswa', views.kelolaBimbinganMahasiswaView, name='kelola-bimbingan-mahasiswa'),
    path('kelola-bimbingan-dosen', views.kelolaBimbinganDosenView, name='kelola-bimbingan-dosen'),
    
]