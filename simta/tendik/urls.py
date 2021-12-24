from django.urls import path
from tendik.views import *
from . import views

urlpatterns = [
    path('', views.dashboardView, name='index'),
    # Laman Pembimbing
    path('pembimbing', views.pembimbingView, name='pembimbing'),
    path('pembimbing/delete/<id>', views.pembimbingHapus, name='pembibmbing-delete'),
    path('pembimbing/editpembimbing/<id>', views.editpembimbing, name='editpembimbing'),

    # -------------------------------------------------------
    # Laman Mahasiswa
    path('mahasiswa', views.mahasiswaView, name='mahasiswa'),
    path('mahasiswa/delete/<id>', views.mahasiswaHapus, name='mahasiswa-delete'),
    path('mahasiswa/editmahasiswa/<id>', views.editmahasiswa, name='editmahasiswa'),
  
    # ------------------------------------------------------
    path('pengajuan-judul', views.pengajuanJudulView, name='pengajuan-judul'),
    path('proposal', views.proposalView, name='proposal'),
    path('tugas-akhir', views.tugasAkhirView, name='tugas-akhir'),
    path('jadwal-bimbingan', views.jadwalBimbingan, name='jadwal-bimbingan'),
    path('jadwal-sempro', views.jadwalSeminarProposal, name='jadwal-sempro'),
    path('jadwal-sidang', views.jadwalSidang, name='jadwal-sidang'),
    # path('kelola-bimbingan-mahasiswa', views.kelolaBimbinganMahasiswaView, name='kelola-bimbingan-mahasiswa'),
    # path('kelola-bimbingan-dosen', views.kelolaBimbinganDosenView, name='kelola-bimbingan-dosen'),
    
]