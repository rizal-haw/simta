from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.apps import apps
from mahasiswa.models import Judul, proposal, ta


class PenyetujuanJudul(models.Model):
    judul = models.ForeignKey(Judul, on_delete=CASCADE)
    keterangan = models.TextField(max_length=500)

class JadwalBimbingan(models.Model):
    date = models.DateField()
    waktu = models.TimeField()
    lokasi = models.CharField(max_length=50)


