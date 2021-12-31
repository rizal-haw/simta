from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE


class pembimbing(models.Model):
    pembimbing_1 = models.TextField(max_length=180)
    pembimbing_2 = models.TextField(max_length=180)
    # pemb = models.ForeignKey(tendik_models, on_delete=models.CASCADE, related_name='pembimbing')

        
class Judul(models.Model):
    # id_pembimbing = models.ForeignKey(pembimbing, on_delete=models.DO_NOTHING, null=True, blank=True)
    judul_1 = models.TextField(max_length=150)
    judul_2 = models.TextField(max_length=150)
    # pembimbing = models.ForeignKey(pembimbing, on_delete=models.DO_NOTHING, null=True, blank=True)

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


    
class bimbingan (models.Model):
    nama = models.CharField(max_length=50)
    nim = models.IntegerField()
    fakultas = models.CharField(max_length=30)
    prodi = models.CharField(max_length=30)
    pembimbing_1 = models.CharField(max_length=20)
    pembimbing_2 = models.CharField(max_length=20)
    judul = models.CharField(max_length=500)
    abstrak = models.CharField(max_length=5000)

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
