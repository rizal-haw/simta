# Generated by Django 3.2.8 on 2021-12-07 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mahasiswa', '0002_auto_20211207_1407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pembimbing',
            name='pembimbing_1',
            field=models.TextField(default='', max_length=180, null=True),
        ),
        migrations.AlterField(
            model_name='pembimbing',
            name='pembimbing_2',
            field=models.TextField(default='', max_length=180, null=True),
        ),
    ]
