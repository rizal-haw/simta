# Generated by Django 3.2.8 on 2021-12-18 15:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tendik', '0007_merge_20211217_2000'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mahasiswamodel',
            name='id_pembimbing',
        ),
    ]
