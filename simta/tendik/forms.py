from django import forms
from django.db.models import fields
from .models import MahasiswaModel

class MahasiswaForm(forms.ModelForm):
    class Meta:
        model = MahasiswaModel

        fields = [
            "nama",
            "nim",
            "prodi",
            "fakultas",
            "kelas",
            "semester",
            "tahun_masuk",
        ]