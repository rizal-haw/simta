<<<<<<< HEAD
# Generated by Django 3.2.10 on 2021-12-29 03:17
=======
# Generated by Django 3.2.9 on 2021-12-29 03:22
>>>>>>> 81706e1d7edcd2e8c45ac4102cd20a5d0abbce57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MahasiswaModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=50)),
                ('nim', models.IntegerField(unique=True)),
                ('prodi', models.CharField(max_length=20)),
                ('fakultas', models.CharField(max_length=20)),
                ('kelas', models.CharField(max_length=3)),
                ('semester', models.IntegerField()),
                ('tahun_masuk', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PembimbingModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=50)),
                ('nip', models.IntegerField(unique=True)),
                ('nidn', models.IntegerField()),
                ('hp', models.BigIntegerField()),
                ('prodi', models.CharField(max_length=20)),
            ],
        ),
    ]
