# Generated by Django 4.2.1 on 2023-07-09 21:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Base_register', '0009_remove_pagosfijos_name'),
    ]

    operations = [
        migrations.DeleteModel(
            name='typePagos',
        ),
        migrations.RemoveField(
            model_name='pagosfijos',
            name='years',
        ),
    ]
