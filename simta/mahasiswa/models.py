from django.db import models
# from simta import tendik
# from tendik.models import pembimbing

class pembimbing(models.Model):
    id_mahasiswa = models.ForeignKey('tendik.PembimbingModel', on_delete=models.DO_NOTHING, null=True, blank=True)
    pembimbing_1 = models.TextField(max_length=180)
    pembimbing_2 = models.TextField(max_length=180)
        
class Judul(models.Model):
    id_mahasiswa = models.ForeignKey('tendik.MahasiswaModel', on_delete=models.DO_NOTHING, null= True, blank=True)
    judul_1 = models.TextField(max_length=150)
    judul_2 = models.TextField(max_length=150)
    # pembimbing = models.ForeignKey(pembimbing, on_delete=models.CASCADE)
    # def __str__(self):
    #     return self.judul_1, self.judul_2

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
    

    
