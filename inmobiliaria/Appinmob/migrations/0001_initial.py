# Generated by Django 4.0.4 on 2022-05-31 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alquiler',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inquilino', models.CharField(max_length=40)),
                ('dueño', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('apellido', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254)),
                ('telefono', models.IntegerField()),
                ('mensaje', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Martillero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('Apellido', models.CharField(max_length=40)),
                ('dni', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Propiedad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titular', models.CharField(max_length=40)),
                ('ubicacion', models.CharField(max_length=40)),
                ('dimensiones', models.CharField(max_length=30)),
                ('poseecartel', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombremartillero', models.CharField(max_length=40)),
                ('comprador', models.CharField(max_length=40)),
            ],
        ),
    ]
