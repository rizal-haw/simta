from django.db import models
from django.db.models.base import Model
from django.db.models.fields import IntegerField
# from mahasiswa.models import Judul, pembimbing

class PembimbingModel(models.Model):
    nip = models.IntegerField(unique=True)
    nidn = models.IntegerField()
    hp = models.BigIntegerField()
    nama = models.CharField(max_length=50)
    prodi = models.CharField(max_length=20)
    # status = models.CharField(max_length=50)
    

class MahasiswaModel(models.Model):
    nim = models.IntegerField(unique=True)
    nama = models.CharField(max_length=50)
    prodi = models.CharField(max_length=20)
    fakultas = models.CharField(max_length=20)
    kelas = models.CharField(max_length=3)
    semester = models.IntegerField()
    tahun_masuk = models.IntegerField(null=True)
    # id_pembimbing = models.ForeignKey(PembimbingModel, on_delete=models.DO_NOTHING, null=True, blank=True)
    

