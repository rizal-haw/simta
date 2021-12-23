from django.db import models
# from tendik import models as tendik_models

class pembimbing(models.Model):
    pembimbing_1 = models.TextField(max_length=180)
    pembimbing_2 = models.TextField(max_length=180)
    # pemb = models.ForeignKey(tendik_models, on_delete=models.CASCADE, related_name='pembimbing')

    # def __str__(self):
    #     return self.pembimbing_1, self.pembimbing_2
        
class Judul(models.Model):
    # id_pembimbing = models.ForeignKey(pembimbing, on_delete=models.DO_NOTHING, null=True, blank=True)
    judul_1 = models.TextField(max_length=150)
    judul_2 = models.TextField(max_length=150)
    # pembimbing = models.ForeignKey(pembimbing, on_delete=models.DO_NOTHING, null=True, blank=True)
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

    
class sempro (models.Model):
    nama = models.CharField(max_length=50)
    nim = models.IntegerField()
    fakultas = models.CharField(max_length=30)
    prodi = models.CharField(max_length=30)
    pembimbing_1 = models.CharField(max_length=20)
    pembimbing_2 = models.CharField(max_length=20)
    judul = models.CharField(max_length=500)
    abstrak = models.CharField(max_length=5000)
