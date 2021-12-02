from django.db import models


class Judul(models.Model):
    judul_1 = models.TextField(max_length=150)
    judul_2 = models.TextField(max_length=150)



class pembimbing(models.Model):
    pembimbing_1 = models.TextField(max_length=180, default='')
    pembimbing_2 = models.TextField(max_length=180, default='')
