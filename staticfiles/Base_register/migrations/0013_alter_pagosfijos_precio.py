# Generated by Django 4.2.1 on 2023-07-09 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Base_register', '0012_alter_cuentacontrybasic_basura_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagosfijos',
            name='precio',
            field=models.CharField(max_length=10),
        ),
    ]
