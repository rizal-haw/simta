from django.db import models

class pembimbing(models.Model):
    pembimbing_1 = models.TextField(max_length=180, default='', null=True)
    pembimbing_2 = models.TextField(max_length=180, default='', null=True)

    def __str__(self):
        return self.pembimbing_1, self.pembimbing_2
        
class Judul(models.Model):
    judul_1 = models.TextField(default='', max_length=150)
    judul_2 = models.TextField(default='', max_length=150)
    pemb_1 = models.ForeignKey(pembimbing, on_delete=models.CASCADE, related_name='sebagai', null=True)

    def __str__(self):
        return self.judul_1, self.judul_2

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
    

    
