from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_tendik = models.BooleanField('Is tendik', default=False)
    is_mhs = models.BooleanField('Is mhs', default=False)
    is_pembimbing = models.BooleanField('Is pembimbing', default=False)
