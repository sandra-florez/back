# Generated by Django 4.1.1 on 2022-09-27 16:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movimientos', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mov_enc_recibos',
            name='cod_persona',
        ),
        migrations.DeleteModel(
            name='mov_det_recibos',
        ),
        migrations.DeleteModel(
            name='mov_enc_recibos',
        ),
    ]
