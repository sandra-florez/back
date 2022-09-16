# Generated by Django 4.1.1 on 2022-09-16 16:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('libros', '0004_alter_cat_autores_cod_autor_and_more'),
        ('personas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='mov_enc_recibos',
            fields=[
                ('cod_recibo', models.DecimalField(decimal_places=0, max_digits=13, primary_key=True, serialize=False)),
                ('fec_recibo', models.DateField()),
                ('cant_recibo', models.SmallIntegerField()),
                ('cant_pendiente', models.SmallIntegerField()),
                ('cod_persona', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='codigoPersonaMov', to='personas.cat_personas')),
            ],
        ),
        migrations.CreateModel(
            name='mov_det_recibos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fec_entrega', models.DateField()),
                ('cant_recibo', models.SmallIntegerField()),
                ('cant_pendiente', models.SmallIntegerField()),
                ('cod_recibo', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='codigoRecibo', to='movimientos.mov_enc_recibos')),
                ('plu', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='Plus', to='libros.cat_libros_plu')),
            ],
        ),
    ]
