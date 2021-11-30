from django.db import models
# from django.db.models.fields import TextField

class Judul(models.Model):
    judul_1 = models.TextField(max_length=150) 
    judul_2 = models.TextField(max_length=150) 

class pembimbing(models.Model):
    pembimbing_1 = models.CharField  (max_length=20, null=False, blank=False)
    pembimbing_1 = models.CharField(max_length=20, null=False, blank=False)
