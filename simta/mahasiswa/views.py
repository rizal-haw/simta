from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from . import models
from django.contrib.auth.decorators import login_required
from django.conf import settings
from tendik import models as tendik_models
from tendik.models import PembimbingModel
from pembimbing.models import PenyetujuanJudul

# @login_required(login_url=settings.LOGIN_URL)
def dashboardViewMhs(request):
    return render(request, 'mhs/index.html')

# ---------------------Halaman Pembibmbing-------------------------------------

def index(request):
    mahasiswa = tendik_models.MahasiswaModel.objects.all()
    pembimbing = tendik_models.PembimbingModel.objects.all()
    pengajuan_judul = models.Judul.objects.all()
    pengajuan_proposal = models.proposal.objects.all()
    pengajuan_ta = models.ta.objects.all()
    bimbingan = models.bimbingan.objects.all()


    jml_mahasiswa = mahasiswa.count()
    jml_pembimbing = pembimbing.count()
    jml_pengajuan_judul = pengajuan_judul.count()
    jml_pengajuan_proposal = pengajuan_proposal.count()
    jml_pengajuan_ta = pengajuan_ta.count()
    jml_bimbingan = bimbingan.count()
    return render (request, 'mhs/index.html', {
        'mahasiswa' : mahasiswa,
        'pembimbing' : pembimbing,
        'pengajuan_judul' : pengajuan_judul,
        'pengajuan_proposal' : pengajuan_proposal,
        'pengajuan_ta' : pengajuan_ta,
        'bimbingan' : bimbingan,
        'jml_mahasiswa' : jml_mahasiswa,
        'jml_pembimbing' : jml_pembimbing,
        'jml_pengajuan_judul' : jml_pengajuan_judul,
        'jml_pengajuan_proposal' : jml_pengajuan_proposal,
        'jml_pengajuan_ta' : jml_pengajuan_ta,
        'jml_bimbingan' : jml_bimbingan })

def pembimbingViewMhs(request):
    if request.POST:

        pembimbing_1 = request.POST['pembimbing_1']
        pembimbing_2 = request.POST['pembimbing_2']
        models.pembimbing.objects.create(
            pembimbing_1 = pembimbing_1, pembimbing_2 = pembimbing_2,)
        print(pembimbing_1)
        print(pembimbing_2)
    input_pembimbing = models.pembimbing.objects.all()
    data_pembimbing =  PembimbingModel.objects.all()
    print(data_pembimbing)
    return render(request,
     'mhs/pembimbing.html', {
        'input_pemb' : input_pembimbing,
        'pembimbing': data_pembimbing,

    })

# End Halaman Pembimbing----------------------------------------------

# ----------------------------Halaman Pengajuan Judul----------------- 

def pengajuanJudulViewMhs(request):
    if request.POST:
        judul_ta = request.POST['judul_ta']
        # judul_2 = request.POST['judul_2']
        models.Judul.objects.create(
            judul_ta=judul_ta)
    data_judul = models.Judul.objects.all()
    penyetujuan_judul = PenyetujuanJudul.objects.all()
    return render(request, 'mhs/pengajuan-judul.html', {
        'judul': data_judul,
        'penyetujuan' : penyetujuan_judul
    })

def hapusJudul(request, id):
    models.Judul.objects.filter(pk = id).delete()
    return redirect('/mhs/pengajuan-judul')

def hapusPembimbing(request, id):
    models.pembimbing.objects.filter(pk =id).delete()
    return redirect('/mhs/pembimbing')
    

# Fungsi disetujui
def penyetujuan(request):
    disetujui = models.PenyetujuanJudul.objects.all()
    konteks = {'data_setuju' : disetujui}
    return render(request, 'mhs/pembimbing.html', konteks)
    
# ----------------------------------------------------
def proposalViewMhs(request):
    if request.POST:
        nama = request.POST['nama']
        nim = request.POST['nim']
        judul = request.POST['judul']
        pembimbing_1 = request.POST['pembimbing_1']
        pembimbing_2 = request.POST['pembimbing_2']
        # models.pembimbing.objects.create(
        #     pembimbing_1 = pembimbing_1, pembimbing_2 = pembimbing_2,)
        # print(pembimbing_1)
        # print(pembimbing_2)
    # data_pembimbing =  PembimbingModel.objects.all()
    # print(data_pembimbing)
    # return render(request, 'mhs/pembimbing.html', {
    #     'pembimbing': data_pembimbing
        models.proposal.objects.create(
         nama = nama, nim = nim, judul= judul, pembimbing_1 = pembimbing_1, pembimbing_2 = pembimbing_2)
         
    data_proposal = models.proposal.objects.all()
    input_pembimbing = models.pembimbing.objects.all()
    data_pembimbing = PembimbingModel.objects.all()
    print(data_proposal)
    return render(request, 'mhs/proposal.html',{
    'proposal': data_proposal,
    'data_pemb' : data_pembimbing,
    'input_pemb' : input_pembimbing })

# -------------------------------------------------------

# ----------------------Halaman TA-----------------------

def TAViewMhs(request):
    if request.POST:
        nim = request.POST['nim']
        nama = request.POST['nama']
        judul = request.POST['judul']
        pembimbing_1 = request.POST['pembimbing_1']
        pembimbing_2 = request.POST['pembimbing_2']
        models.ta.objects.create(
         nama = nama, nim = nim, judul= judul, pembimbing_1 = pembimbing_1, pembimbing_2 = pembimbing_2)
         
    data_ta = models.ta.objects.all()
    input_pembimbing = models.pembimbing.objects.all()
    data_pembimbing = PembimbingModel.objects.all()
    print(data_ta)
    return render(request, 'mhs/tugas-akhir.html', {
    'ta': data_ta,
    'data_pemb' : data_pembimbing,
    'input_pemb' : input_pembimbing })

def seminarproposalViewMhs(request):
    if request.POST:
        nama = request.POST['nama']
        nim = request.POST['nim']
        fakultas = request.POST['fakultas']
        prodi = request.POST['prodi']
        pembimbing_1 = request.POST['pembimbing_1']
        pembimbing_2 = request.POST['pembimbing_2']
        judul = request.POST['judul']
        abstrak = request.POST['abstrak']
        models.sempro.objects.create(
            nama=nama, nim=nim, fakultas=fakultas, prodi=prodi, pembimbing_1=pembimbing_1, pembimbing_2=pembimbing_2, judul=judul, abstrak=abstrak)

    data_sempro = models.sempro.objects.all()
    input_pembimbing = models.pembimbing.objects.all()
    data_pembimbing = PembimbingModel.objects.all()
    print (data_sempro)
    return render(request, 'mhs/seminar-proposal.html',{
        'sempro': data_sempro,
        'data_pemb' : data_pembimbing,
        'input_pemb' : input_pembimbing })


# def bimbinganViewMhs(request):
#     if request.POST:
#         nama = request.POST['nama']
#         nim = request.POST['nim']
#         fakultas = request.POST['fakultas']
#         prodi = request.POST['prodi']
#         pembimbing_1 = request.POST['pembimbing_1']
#         pembimbing_2 = request.POST['pembimbing_2']
#         judul = request.POST['judul']
#         abstrak = request.POST['abstrak']
#         models.bimbingan.objects.create(
#             nama=nama, nim=nim, fakultas=fakultas, prodi=prodi, pembimbing_1=pembimbing_1, pembimbing_2=pembimbing_2, judul=judul, abstrak=abstrak)
#     data_bimbingan = models.bimbingan.objects.all()
#     input_pembimbing = models.pembimbing.objects.all()
#     data_pembimbing = PembimbingModel.objects.all()
#     print (data_bimbingan)
#     return render(request, 'mhs/bimbingan.html',{
#         'bimbingan': data_bimbingan ,
#         'data_pemb' : data_pembimbing,
#         'input_pemb' : input_pembimbing })

def sidangskripsiViewMhs(request):
    if request.POST:
        nama = request.POST['nama']
        nim = request.POST['nim']
        fakultas = request.POST['fakultas']
        prodi = request.POST['prodi']
        pembimbing_1 = request.POST['pembimbing_1']
        pembimbing_2 = request.POST['pembimbing_2']
        judul = request.POST['judul']
        abstrak = request.POST['abstrak']
        models.sidang.objects.create(
            nama=nama, nim=nim, fakultas=fakultas, prodi=prodi, pembimbing_1=pembimbing_1, pembimbing_2=pembimbing_2, judul=judul, abstrak=abstrak)
    data_sidang = models.sidang.objects.all()
    input_pembimbing = models.pembimbing.objects.all()
    data_pembimbing = PembimbingModel.objects.all()
    print (data_sidang)
    return render(request, 'mhs/sidang-skripsi.html',{
        'sidang': data_sidang ,
        'data_pemb' : data_pembimbing,
        'input_pemb' : input_pembimbing })

def bukupanduanViewMhs(request):
    return render(request, 'mhs/buku-panduan.html')

def formulirViewMhs(request):
    return render(request, 'mhs/formulir.html')


