from django.db import models


class Judul(models.Model):
    judul_1 = models.TextField(max_length=150)
    judul_2 = models.TextField(max_length=150)



class pembimbing(models.Model):
    pembimbing_1 = models.TextField(max_length=180, default='')
    pembimbing_2 = models.TextField(max_length=180, default='')

class proposal(models.Model):
    nama = models.CharField(max_length=50)
    nim = models.IntegerField()
    judul = models.CharField(max_length=200)
    pembimbing_1 = models.CharField(max_length=20)
    pembimbing_2 = models.CharField(max_length=20)

class ta (models.Model):
    nim = models.IntegerField()
    nama = models.CharField(max_length=50)
    judul = models.CharField(max_length=200)
    pembimbing_1 = models.CharField(max_length=20)
    pembimbing_2 = models.CharField(max_length=20)
    

    
