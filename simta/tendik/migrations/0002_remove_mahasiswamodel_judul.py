# Generated by Django 3.2.8 on 2021-12-30 19:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tendik', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mahasiswamodel',
            name='judul',
        ),
    ]
