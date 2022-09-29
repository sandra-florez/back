# Generated by Django 4.1.1 on 2022-09-28 16:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0011_remove_cat_estados_per_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cat_personas',
            name='cod_estado_per',
            field=models.ForeignKey(default='NOR', on_delete=django.db.models.deletion.RESTRICT, related_name='codigoEstadoPersona', to='personas.cat_estados_per'),
        ),
    ]
