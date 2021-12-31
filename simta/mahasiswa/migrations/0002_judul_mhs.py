# Generated by Django 3.2.8 on 2021-12-30 19:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tendik', '0002_remove_mahasiswamodel_judul'),
        ('mahasiswa', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='judul',
            name='mhs',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='tendik.mahasiswamodel'),
        ),
    ]
