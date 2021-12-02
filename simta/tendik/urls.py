from django.urls import path
from tendik.views import *
from . import views

urlpatterns = [
    path('', views.dashboardView, name='index'),
    # Laman Pembimbing
    path('pembimbing', views.pembimbingView, name='pembimbing'),
    path('pembimbing/delete/<id>', views.pembimbingHapus, name='pembibmbing-delete'),
    # -------------------------------------------------------
    # Laman Mahasiswa
    path('mahasiswa', views.mahasiswaView, name='mahasiswa'),
    path('mahasiswa/delete/<id>', views.mahasiswaHapus, name='mahasiswa'),
    # ------------------------------------------------------
    path('pengajuan-judul', views.pengajuanJudulView, name='pengajuan-judl'),
    path('proposal', views.proposalView, name='proposal'),
    path('tugas-akhir', views.tugasAkhirView, name='tugas-akhir'),
    # path('kelola-bimbingan-mahasiswa', views.kelolaBimbinganMahasiswaView, name='kelola-bimbingan-mahasiswa'),
    # path('kelola-bimbingan-dosen', views.kelolaBimbinganDosenView, name='kelola-bimbingan-dosen'),
    
]