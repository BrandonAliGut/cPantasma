from typing import Any
from django.db import models
from User.models import User_Perfil
from django.db.models.signals import post_save
import time
''''''
# Create your models here.


class Cobrador(models.Model):

    Perfil_for    = models.ForeignKey(User_Perfil, on_delete=models.CASCADE, blank=True)
    data_at         = models.DateField(auto_now_add=True)
    update_at       = models.DateField()
    def __str__(self):
        return str(self.Perfil_for.Nombre)
    


   

class Contribuyente(models.Model):
    register_for= models.ForeignKey(Cobrador, on_delete=models.CASCADE, blank=True, null=True)
    nombre      = models.CharField(blank=True, max_length=100)
    codigo      = models.IntegerField(blank=True, null=True)
    N_cedula    = models.CharField(max_length=255,blank=True, null=True)
    Comunidad   = models.CharField(blank=True, max_length=60)
    Direccion   = models.TextField(blank=True, max_length=100)
    data_at     = models.DateField(auto_now_add=True)
    update_at   = models.DateField()
    def __str__(self):
        return str(self.nombre)
class Ordering(models.Model):
    
    abs_apellido=[ ('A','A'),
                  ('B','B'),
                  ('C','C'),
                  ('D','D'), 
                  ('E','E'), 
                  ('F','F'), 
                  ('G','G'), 
                  ('H','H'),
                  ('I','I'),
                  ('CH',"CH"),
                    ('J','J'), 
                    ('K','K'), 
                    ('L','L'), 
                    ('M','M'), 
                    ('N','N'), 
                    ('O','O'), 
                    ('P','P'), 
                    ('Q','Q'), 
                    ('R','R'), 
                    ('S','S'),
                    ('T','T'), 
                    ('U','U'), 
                    ('V','V'), 
                    ('W','W'), 
                    ('X','X'), 
                    ('Y','Y'), 
                    ('Z','Z'),
                ]
    contryUnique = models.OneToOneField(Contribuyente, on_delete=models.CASCADE, blank=True, null=True)
    type_abs = models.CharField(max_length=2, choices=abs_apellido, blank=False)
    primer_apellido = models.CharField(blank=True, max_length=100)
    complete_name = models.IntegerField(blank=True, null=True)
    
    id_type_abs = models.IntegerField(blank=False, null=False)
    id_primer_apellido = models.IntegerField(blank=False, null=False)
    id_complete_name = models.IntegerField(blank=False, null=False)

class Years(models.Model):
    year = models.IntegerField(unique=True)
    def __str__(self):
        return str(self.year)

class Months(models.Model):
    years   = models.ForeignKey(Years, on_delete=models.CASCADE)
    people  = models.ForeignKey(Contribuyente, on_delete=models.CASCADE)
    enero   = models.BooleanField(default=False)
    feb     = models.BooleanField(default=False)
    mar     = models.BooleanField(default=False)
    abril   = models.BooleanField(default=False)
    may     = models.BooleanField(default=False)
    Juni    = models.BooleanField(default=False)
    Juli    = models.BooleanField(default=False)
    Agos    = models.BooleanField(default=False)
    Sep     = models.BooleanField(default=False)
    Octu    = models.BooleanField(default=False)
    Nov     = models.BooleanField(default=False)
    Dic     = models.BooleanField(default=False)
    def __str__(self):
        return str(self.people.nombre)
    
class UpdateMonthsContry(models.Model):
    update  = models.ForeignKey(Months, on_delete=models.CASCADE)
    data_at = models.DateField(auto_now_add=True)
    def __str__(self):
        return str(self.update.years.year)
    


    
class CuentasPagos(models.Model):
    cuenta      = models.CharField(max_length=50, blank=True)
    code_max        = models.CharField(max_length=18, blank=False)
    min_code        = models.CharField(max_length=6, blank=False)
    p_year          = models.BooleanField(default= False, help_text="este campo solo se aplica en pagos anuales")
    def __str__(self):
        return str(self.cuenta)
    
class Empresa(models.Model):
    name_empresa = models.CharField(max_length=255, blank=False, null=False)
    Direcion  = models.CharField(max_length=255, blank=False, null=False)
    def __str__(self):
        return str(self.name_empresa)
class PagoCuenta(models.Model):
    empresa   = models.ForeignKey(Empresa, on_delete=models.CASCADE, blank=True, null=True)
    contribuyente   = models.ForeignKey(Contribuyente, on_delete=models.CASCADE, blank=True, null=True)
    cuenta_pago     = models.ForeignKey(CuentasPagos, on_delete=models.CASCADE, blank=True, null=True)
    cantidad        = models.IntegerField(max_length=3, blank=True)
    activo          = models.BooleanField(default=True)
    data_at         = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return str(self.cuenta_pago)


    
    

    
def historial(sender, **kwargs,):
    months = kwargs['instance']
   
    if kwargs["created"]:
        months_contry = UpdateMonthsContry(update=months)
        months_contry.save()
post_save.connect(historial, sender=Months)