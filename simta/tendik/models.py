from django.db import models
from django.db.models.base import Model
from django.db.models.fields import IntegerField
from mahasiswa.models import Judul, pembimbing

class PembimbingModel(models.Model):
    nama = models.CharField(max_length=50)
    nip = models.IntegerField(unique=True)
    nidn = models.IntegerField()
    hp = models.BigIntegerField()
    prodi = models.CharField(max_length=20)
    

    def __str__(self):
        return self.nama

class MahasiswaModel(models.Model):
    nama = models.CharField(max_length=50)
    nim = models.IntegerField(unique=True)
    prodi = models.CharField(max_length=20)
    fakultas = models.CharField(max_length=20)
    kelas = models.CharField(max_length=3)
    semester = models.IntegerField()
    tahun_masuk = models.IntegerField(null=True)
    # id_pembimbing = models.ForeignKey(PembimbingModel, on_delete=models.DO_NOTHING, null=True, blank=True)
    

