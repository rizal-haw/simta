# Generated by Django 3.2.8 on 2021-12-27 09:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mahasiswa', '0002_auto_20211227_1608'),
        ('pembimbing', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PenyetujuanJudul',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keterangan', models.TextField(max_length=500)),
                ('judul', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mahasiswa.judul')),
            ],
        ),
    ]
