from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from tendik.models import Mahasiswa
from tendik.models import DosenPemb


class Pembimbing(models.Model):
    pembimbing_1 = models.TextField(max_length=180, default="")
    pembimbing_2 = models.TextField(max_length=180, default="")
    id_pemb = models.ForeignKey(DosenPemb, on_delete=models.CASCADE, related_name='Dosen', blank=True, null=True)
        
class Judul(models.Model):
    id_pembimbing = models.ForeignKey(Pembimbing, on_delete=models.CASCADE, null=True, blank=True)
    id_mhs = models.ForeignKey(Mahasiswa, on_delete=CASCADE, blank=True, null=True)
    judul = models.TextField(max_length=150, default="")
    latar_belakang = models.TextField(max_length=500, default="")
    rumusan_masalah = models.TextField(max_length=500, default="")
    batasan = models.TextField(max_length=500, default="")
    # judul_2 = models.TextField(max_length=150, default="")
    keterangan = models.TextField(max_length=500, default="")
    tolak = models.CharField(max_length=6, default="")
    status_judul = models.CharField(max_length=20, default="Pending")
    date_judul = models.DateField(blank=True, null=True)
    date_disetujui = models.DateField(blank=True, null=True)

class Proposal(models.Model):
    nama = models.CharField(max_length=50)
    nim = models.IntegerField()
    judul = models.CharField(max_length=200)
    pembimbing_1 = models.TextField(max_length=180)
    pembimbing_2 = models.TextField(max_length=180)

class Ta (models.Model):
    nim = models.IntegerField()
    nama = models.CharField(max_length=50)
    judul = models.CharField(max_length=200)
    pembimbing_1 = models.TextField(max_length=180)
    pembimbing_2 = models.TextField(max_length=180)


    

class sempro (models.Model):
    nama = models.CharField(max_length=50)
    nim = models.IntegerField()
    fakultas = models.CharField(max_length=30)
    prodi = models.CharField(max_length=30)
    pembimbing_1 = models.CharField(max_length=20)
    pembimbing_2 = models.CharField(max_length=20)
    judul = models.CharField(max_length=500)
    abstrak = models.CharField(max_length=5000)

class sidang (models.Model):
    nama = models.CharField(max_length=50)
    nim = models.IntegerField()
    fakultas = models.CharField(max_length=30)
    prodi = models.CharField(max_length=30)
    pembimbing_1 = models.CharField(max_length=20)
    pembimbing_2 = models.CharField(max_length=20)
    judul = models.CharField(max_length=500)
    abstrak = models.CharField(max_length=5000)
