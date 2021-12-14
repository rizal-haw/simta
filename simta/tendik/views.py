from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from . import models
from .forms import MahasiswaForm

def dashboardView(request):
    return render(request, 'tendik/index.html')

# ----------------------Untuk Halaman Pembimbing-------------------------------------------------

# Menampilkan data inputan

def pembimbingView(request):
    if request.POST:
        nama = request.POST['nama']
        nip = request.POST['nip']
        nidn = request.POST['nidn']
        hp = request.POST['hp']
        prodi = request.POST['prodi']
        models.PembimbingModel.objects.create(nama=nama, nip=nip, nidn=nidn, hp=hp, prodi=prodi)
    pembibmbing_table = models.PembimbingModel.objects.all()
    return render(request, 'tendik/pembimbing.html', {
        'pemb_table': pembibmbing_table
    })

# Hapus

def pembimbingHapus(request, id):
    models.PembimbingModel.objects.filter(pk =id).delete()
    return redirect('/tendik/pembimbing')

# ------------------------------------------------------------------------------

# ----------------------Untuk Halaman Mahasiswa---------------------------------

# Tampilkan Data
def mahasiswaView(request):
    if request.POST:
        nama = request.POST['nama']
        nim = request.POST['nim']
        prodi = request.POST['prodi']
        fakultas = request.POST['fakultas']
        kelas = request.POST['kelas']
        semester = request.POST['semester']
        tahun_masuk = request.POST['tahun_masuk']
        models.MahasiswaModel.objects.create(nama=nama, nim=nim, prodi=prodi, fakultas=fakultas, kelas=kelas, semester=semester, tahun_masuk=tahun_masuk)
        print(nim)
        
    mhs_table = models.MahasiswaModel.objects.all()
    return render(request, 'tendik/mahasiswa.html', {
        'tabel_mhs': mhs_table
    })

# Update
def mahasiswaUpdate(request, id):
    if request.POST:
        models.MahasiswaModel.objects.filter(pk=id).first(
            nama = request.POST['nama'],
            nim = request.POST['nim'],
            prodi = request.POST['prodi'],
            fakultas = request.POST['fakultas'],
            kelas = request.POST['kelas'],
            semester = request.POST['semester'],
            tahun_masuk = request.POST['tahun_masuk'],
        )
    mhs_update = models.MahasiswaModel.objects.filter(pk=id).first()
    return render(request, 'tendik/mahasiswa', {
        'mhs_update': mhs_update
    })

    # Hapus Data
def mahasiswaHapus(request, id):
    models.MahasiswaModel.objects.filter(pk=id).delete()
    return redirect('/tendik/mahasiswa')

# ------------------------------------------------------------

def pengajuanJudulView(request):
    data_judul = models.Judul.objects.all()
    konteks = {'data_judul' : data_judul}
    return render(request, 'tendik/pengajuanjudul.html', konteks)

def proposalView(request):
    data_judul = models.Judul.objects.all()
    konteks = {'data_judul' : data_judul}
    return render(request, 'tendik/proposal.html', konteks)

def tugasAkhirView(request):
    return render(request, 'tendik/tugas-akhir.html')

def jadwalBimbingan(request):
    return render(request, 'tendik/jadwal-bimbingan.html')

def jadwalSidang(request):
    return render(request, 'tendik/jadwal-sidang.html')