from django.db import models


class Judul(models.Model):
    judul_1 = models.TextField(max_length=150) 
    judul_2 = models.TextField(max_length=150) 
