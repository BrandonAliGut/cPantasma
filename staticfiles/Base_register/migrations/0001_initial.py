# Generated by Django 4.2.1 on 2023-06-08 12:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cobrador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_at', models.DateField(auto_now_add=True)),
                ('update_at', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Contribuyente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=100)),
                ('codigo', models.IntegerField(blank=True, null=True)),
                ('N_cedula', models.CharField(blank=True, max_length=255, null=True)),
                ('Comunidad', models.CharField(blank=True, max_length=60)),
                ('Direccion', models.TextField(blank=True, max_length=100)),
                ('data_at', models.DateField(auto_now_add=True)),
                ('update_at', models.DateField()),
                ('register_for', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Base_register.cobrador')),
            ],
        ),
        migrations.CreateModel(
            name='Months',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enero', models.BooleanField(default=False)),
                ('feb', models.BooleanField(default=False)),
                ('mar', models.BooleanField(default=False)),
                ('abril', models.BooleanField(default=False)),
                ('may', models.BooleanField(default=False)),
                ('Juni', models.BooleanField(default=False)),
                ('Juli', models.BooleanField(default=False)),
                ('Agos', models.BooleanField(default=False)),
                ('Sep', models.BooleanField(default=False)),
                ('Octu', models.BooleanField(default=False)),
                ('Nov', models.BooleanField(default=False)),
                ('Dic', models.BooleanField(default=False)),
                ('people', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Base_register.contribuyente')),
            ],
        ),
        migrations.CreateModel(
            name='typeNegocio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='typePagos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Years',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='UpdateMonthsContry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_at', models.DateField(auto_now_add=True)),
                ('update', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Base_register.months')),
            ],
        ),
        migrations.CreateModel(
            name='pagosFijos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precio', models.CharField(blank=True, max_length=10)),
                ('name', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Base_register.typepagos')),
                ('negocio', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Base_register.typenegocio')),
                ('people', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Base_register.contribuyente')),
                ('years', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Base_register.years')),
            ],
        ),
        migrations.AddField(
            model_name='months',
            name='years',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Base_register.years'),
        ),
    ]
