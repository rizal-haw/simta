from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from . import models
from django.contrib.auth.decorators import login_required
from django.conf import settings
from simta.settings import cursor


# @login_required(login_url=settings.LOGIN_URL)
def dashboardViewPembimbing(request):
#     mahasiswa = tendik_models.MahasiswaModel.objects.all()
#     pembimbing = tendik_models.PembimbingModel.objects.all()
#     pengajuan_judul = models.Judul.objects.all()
#     pengajuan_proposal = models.proposal.objects.all()
#     pengajuan_ta = models.ta.objects.all()
#     bimbingan = models.bimbingan.objects.all()


#     jml_mahasiswa = mahasiswa.count()
#     jml_pembimbing = pembimbing.count()
#     jml_pengajuan_judul = pengajuan_judul.count()
#     jml_pengajuan_proposal = pengajuan_proposal.count()
#     jml_pengajuan_ta = pengajuan_ta.count()
#     jml_bimbingan = bimbingan.count()
    return render(request, 'pembimbing/index.html')
#         'mahasiswa' : mahasiswa,
#         'pembimbing' : pembimbing,
#         'pengajuan_judul' : pengajuan_judul,
#         'pengajuan_proposal' : pengajuan_proposal,
#         'pengajuan_ta' : pengajuan_ta,
#         'bimbingan' : bimbingan,
#         'jml_mahasiswa' : jml_mahasiswa,
#         'jml_pembimbing' : jml_pembimbing,
#         'jml_pengajuan_judul' : jml_pengajuan_judul,
#         'jml_pengajuan_proposal' : jml_pengajuan_proposal,
#         'jml_pengajuan_ta' : jml_pengajuan_ta,
#         'jml_bimbingan' : jml_bimbingan })

def pembimbingViewPembimbing(request):
    return render(request, 'pembimbing/pembimbing.html')

# ---------------Halaman Pengajuan Judul-----------------

# def DataPengajuanJudul(request):

#     # Query join
#     query = "SELECT mhs.nama, mhs.nim, j.judul_1, j.judul_2 FROM public.mahasiswa_judul as j JOIN public.tendik_mahasiswamodel as mhs ON j.mhs_id=mhs.id "
#     cursor.execute(query)
#     data_pengajuan = cursor.fetchall()

#     data = {
#         'data_pengajuan': data_pengajuan,
#     }

#     return render(request, 'pembimbing/pengajuan-judul.html', {'data': data})

def pengajuanJudulViewPembimbing(request):
    # Query join
    query = "SELECT mhs.nama, mhs.nim, j.judul_1, j.judul_2 FROM public.mahasiswa_judul as j JOIN public.tendik_mahasiswamodel as mhs ON j.mhs_id=mhs.id "
    cursor.execute(query)
    data_pengajuan = cursor.fetchall()

    if request.method == 'POST':
        get_judul = request.POST['judul']
        keterangan = request.POST['keterangan']

        judul_input = models.Judul.objects.filter(id=get_judul).first()
        models.PenyetujuanJudul.objects.create(judul=judul_input, keterangan=keterangan)

    data_judul = models.Judul.objects.all()
    penyetujuan = models.PenyetujuanJudul.objects.all()
    konteks = {'data_judul' : data_judul, 'penyetujuan' : penyetujuan, 'data_pengajuan': data_pengajuan}

    return render(request, 'pembimbing/pengajuan-judul.html', {'konteks' : konteks})

# Detail Judul
def detailJudul(request, id):
    detail_judul = models.Judul.objects.filter(id = id).first()
    konteks = {'detail_judul': detail_judul}
    return render(request, 'pembimbing/detail-judul.html', konteks)
# -------end----------------------------------------------

# -------Halaman Pengajuan Proposal------------------------

def pengajuanProposalViewPembimbing(request):
    data_proposal = models.proposal.objects.all()
    konteks = {'data_proposal': data_proposal}
    return render(request, 'pembimbing/pengajuan-proposal.html', konteks)
# --------End-----------------------------------------------

def pengajuanTAViewPembimbing(request):
    data_ta = models.ta.objects.all()
    konteks = {'data_ta': data_ta}
    return render(request, 'pembimbing/pengajuan-ta.html',konteks)

# -----------Halaman Permintaan Bimbingan------------------------

def permintaanBimbinganViewPembimbing(request):
    if request.POST:
        models.JadwalBimbingan.objects.create(
            date = request.POST['date'],
            waktu = request.POST['waktu'],
            lokasi = request.POST['lokasi'],
        )
    jadwalBimbing = models.JadwalBimbingan.objects.all()
    konteks = {'jadwalBimbing': jadwalBimbing}
    return render(request, 'pembimbing/permintaan-bimbingan.html', konteks)

# -------------End-----------------------------------------------


def bimbinganTAViewPembimbing(request):
    return render(request, 'pembimbing/bimbingan-ta.html')

def jadwalTAViewPembimbing(request):
    return render(request, 'pembimbing/jadwal.html')

def panduanTAViewPembimbing(request):
    return render(request, 'pembimbing/panduan.html')
