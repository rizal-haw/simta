from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.apps import apps
from django.db.models.expressions import Case
from mahasiswa.models import Judul, Proposal, Ta
from tendik.models import Mahasiswa


class JadwalBimbingan(models.Model):
    date = models.DateField()
    waktu = models.TimeField()
    lokasi = models.CharField(max_length=50)


