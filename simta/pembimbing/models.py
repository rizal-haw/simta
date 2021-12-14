from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from mahasiswa.models import Judul, proposal

class JadwalBimbingan(models.Model):
    date = models.DateField()
    waktu = models.TimeField()
    lokasi = models.CharField(max_length=50)


