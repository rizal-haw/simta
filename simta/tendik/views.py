from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from . import models
from mahasiswa import models as models_mhs
from .forms import MahasiswaForm
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib import messages
# from mahasiswa.models import Judul, pembimbing

# @login_required(login_url=settings.LOGIN_URL)
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
        messages.success(request, f'Data pembimbing berhasil ditambahkan')
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
        messages.success(request, f'Data Mahasiswa telah ditambahkan')
        print(nim)
        
    mhs_table = models.MahasiswaModel.objects.all()
    return render(request, 'tendik/mahasiswa.html', {
        'tabel_mhs': mhs_table
    })

    # Hapus Data
def mahasiswaHapus(request, id):
    models.MahasiswaModel.objects.filter(pk=id).delete()
    return redirect('/tendik/mahasiswa')

    # edit mahasiswa
def editmahasiswa(request, id):
    if request.POST:
        models.MahasiswaModel.objects.filter(pk=id).update(
            nama = request.POST['nama'],
            nim = request.POST['nim'],
            prodi = request.POST['prodi'],
            fakultas = request.POST['fakultas'],
            kelas = request.POST['kelas'],
            semester = request.POST['semester'],
            tahun_masuk = request.POST['tahun_masuk'],
        )
        return redirect ('/tendik/mahasiswa')
    mhs_update = models.MahasiswaModel.objects.filter(pk=id).first()
    print(mhs_update)
    return render(request, 'tendik/editmahasiswa.html', {
        'tabel_mhs': mhs_update
    })


    # edit pembimbing
def editpembimbing(request, id):
    if request.POST:
        models.PembimbingModel.objects.filter(pk=id).update(
            nama = request.POST['nama'],
            nip = request.POST['nip'],
            nidn = request.POST['nidn'],
            hp = request.POST['hp'],
            prodi = request.POST['prodi'],
        )
        return redirect ('/tendik/pembimbing')
    pembimbing_update = models.PembimbingModel.objects.filter(pk=id).first()
    print(pembimbing_update)
    return render(request, 'tendik/editpembimbing.html', {
        'tabel_mhs': pembimbing_update
    })

    #  return render(request, 'tendik/editmahasiswa.html')

# ------------------------------------------------------------

def pengajuanJudulView(request):
    data_judul = models.Judul.objects.all()
    # data_pem = models_mhs.pembimbing.objects.all()
    # print(data_pem)
    konteks = {'data_judul' : data_judul}
    # konteks2 = {'datapem' : data_pem}
    return render(request, 'tendik/pengajuanjudul.html', konteks)

def proposalView(request):
    data_pembimbing = models.pembimbing.objects.all()
    konteks2 = {'data_pembimbing' : data_pembimbing}
    return render(request, 'tendik/proposal.html', konteks2)

def tugasAkhirView(request):
    return render(request, 'tendik/tugas-akhir.html')

def jadwalBimbingan(request):
    return render(request, 'tendik/jadwal-bimbingan.html')

def jadwalSeminarProposal(request):
    return render(request, 'tendik/jadwal-sempro.html')

def jadwalSidang(request):
    return render(request, 'tendik/jadwal-sidang.html')