from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.apps import apps
from django.db.models.expressions import Case
from mahasiswa.models import Judul, Proposal, Ta
from tendik.models import Mahasiswa

class PenyetujuanJudul(models.Model):
    judul = models.CharField(max_length=20, default='')
    keterangan = models.TextField(max_length=500, default='')
    judul_id = models.ForeignKey(Judul, on_delete=CASCADE, blank=True, null=True)

class JadwalBimbingan(models.Model):
    date = models.DateField()
    waktu = models.TimeField()
    lokasi = models.CharField(max_length=50)


