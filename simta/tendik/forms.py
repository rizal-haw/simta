from django import forms
from django.db.models import fields
from .models import Mahasiswa

class MahasiswaForm(forms.ModelForm):
    class Meta:
        model = Mahasiswa

        fields = [
            "nama",
            "nim",
            "prodi",
            "fakultas",
            "kelas",
            "semester",
            "tahun_masuk",
        ]