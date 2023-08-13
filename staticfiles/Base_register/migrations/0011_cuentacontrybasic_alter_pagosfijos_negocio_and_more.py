# Generated by Django 4.2.1 on 2023-07-09 21:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Base_register', '0010_delete_typepagos_remove_pagosfijos_years'),
    ]

    operations = [
        migrations.CreateModel(
            name='CuentaContryBasic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Negocio', models.CharField(max_length=50, unique=True)),
                ('IMI', models.CharField(max_length=50, unique=True)),
                ('Basura', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='pagosfijos',
            name='negocio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Base_register.cuentacontrybasic'),
        ),
        migrations.DeleteModel(
            name='typeNegocio',
        ),
    ]
