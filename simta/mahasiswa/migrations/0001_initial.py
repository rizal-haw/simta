# Generated by Django 3.2.8 on 2022-01-01 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='bimbingan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=50)),
                ('nim', models.IntegerField()),
                ('fakultas', models.CharField(max_length=30)),
                ('prodi', models.CharField(max_length=30)),
                ('pembimbing_1', models.CharField(max_length=20)),
                ('pembimbing_2', models.CharField(max_length=20)),
                ('judul', models.CharField(max_length=500)),
                ('abstrak', models.CharField(max_length=5000)),
            ],
        ),
        migrations.CreateModel(
            name='Judul',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('judul_1', models.TextField(max_length=150)),
                ('judul_2', models.TextField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Pembimbing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pembimbing_1', models.TextField(max_length=180)),
                ('pembimbing_2', models.TextField(max_length=180)),
            ],
        ),
        migrations.CreateModel(
            name='Proposal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=50)),
                ('nim', models.IntegerField()),
                ('judul', models.CharField(max_length=200)),
                ('pembimbing_1', models.TextField(max_length=180)),
                ('pembimbing_2', models.TextField(max_length=180)),
            ],
        ),
        migrations.CreateModel(
            name='sempro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=50)),
                ('nim', models.IntegerField()),
                ('fakultas', models.CharField(max_length=30)),
                ('prodi', models.CharField(max_length=30)),
                ('pembimbing_1', models.CharField(max_length=20)),
                ('pembimbing_2', models.CharField(max_length=20)),
                ('judul', models.CharField(max_length=500)),
                ('abstrak', models.CharField(max_length=5000)),
            ],
        ),
        migrations.CreateModel(
            name='sidang',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=50)),
                ('nim', models.IntegerField()),
                ('fakultas', models.CharField(max_length=30)),
                ('prodi', models.CharField(max_length=30)),
                ('pembimbing_1', models.CharField(max_length=20)),
                ('pembimbing_2', models.CharField(max_length=20)),
                ('judul', models.CharField(max_length=500)),
                ('abstrak', models.CharField(max_length=5000)),
            ],
        ),
        migrations.CreateModel(
            name='Ta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nim', models.IntegerField()),
                ('nama', models.CharField(max_length=50)),
                ('judul', models.CharField(max_length=200)),
                ('pembimbing_1', models.TextField(max_length=180)),
                ('pembimbing_2', models.TextField(max_length=180)),
            ],
        ),
    ]
