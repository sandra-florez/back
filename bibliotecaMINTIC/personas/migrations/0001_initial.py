# Generated by Django 4.1.1 on 2022-09-16 16:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cat_cargos',
            fields=[
                ('cod_cargo', models.SmallIntegerField(primary_key=True, serialize=False)),
                ('des_cargo', models.CharField(max_length=45)),
                ('cod_estado', models.CharField(max_length=3)),
                ('sw_empleado', models.SmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='cat_estados_per',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cod_estado_per', models.CharField(max_length=3)),
                ('des_estado_per', models.CharField(max_length=45)),
                ('sw_activo', models.SmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='cat_personas',
            fields=[
                ('cod_persona', models.AutoField(primary_key=True, serialize=False)),
                ('tipo_documento', models.CharField(max_length=3)),
                ('num_documento', models.CharField(max_length=25)),
                ('nombres', models.CharField(max_length=45)),
                ('apellidos', models.CharField(max_length=45)),
                ('dirección', models.CharField(max_length=45)),
                ('tel_movil', models.PositiveIntegerField()),
                ('des_municipio', models.CharField(max_length=55)),
                ('email', models.EmailField(max_length=254)),
                ('fec_nacimiento', models.DateField()),
                ('fec_ingreso', models.DateField()),
                ('cod_cargo', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='codigoCargo', to='personas.cat_cargos')),
                ('cod_estado_per', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='codigoEstadoPersona', to='personas.cat_estados_per')),
            ],
        ),
        migrations.CreateModel(
            name='cat_accesos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=25)),
                ('clave', models.CharField(max_length=255)),
                ('fec_cambio', models.DateField()),
                ('cod_persona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='codigoPersona', to='personas.cat_personas')),
            ],
        ),
    ]
