from django.db import models
# from django.db.models.fields import TextField

class Judul(models.Model):
    judul_1 = models.TextField(max_length=150) 
    judul_2 = models.TextField(max_length=150) 
