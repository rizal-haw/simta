from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.apps import apps
from django.db.models.expressions import Case
from mahasiswa.models import Judul, proposal, ta
from tendik.models import MahasiswaModel

# class DataPengajuanJudul(models.Model):
#     data_diri = models.ForeignKey(MahasiswaModel, on_delete=CASCADE)
#     isi_judul = models.ForeignKey(Judul, on_delete=CASCADE)


class PenyetujuanJudul(models.Model):
    judul = models.ForeignKey(Judul, on_delete=CASCADE)
    keterangan = models.TextField(max_length=500)

class JadwalBimbingan(models.Model):
    date = models.DateField()
    waktu = models.TimeField()
    lokasi = models.CharField(max_length=50)


