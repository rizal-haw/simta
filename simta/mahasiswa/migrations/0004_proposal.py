# Generated by Django 3.2.9 on 2021-12-02 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mahasiswa', '0003_auto_20211202_1105'),
    ]

    operations = [
        migrations.CreateModel(
            name='proposal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=50)),
                ('NIM', models.IntegerField()),
                ('judul', models.CharField(max_length=200)),
                ('pembimbing_1', models.CharField(max_length=20)),
                ('pembimbing_2', models.CharField(max_length=20)),
            ],
        ),
    ]
