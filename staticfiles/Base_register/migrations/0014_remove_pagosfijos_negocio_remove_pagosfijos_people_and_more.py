# Generated by Django 4.2.1 on 2023-07-09 22:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Base_register', '0013_alter_pagosfijos_precio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pagosfijos',
            name='negocio',
        ),
        migrations.RemoveField(
            model_name='pagosfijos',
            name='people',
        ),
        migrations.DeleteModel(
            name='CuentaContryBasic',
        ),
        migrations.DeleteModel(
            name='pagosFijos',
        ),
    ]
