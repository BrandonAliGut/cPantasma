from django import forms
from Base_register.models import *
'''
class Contribuyente(forms.ModelForm):
    
    
    
    register_for= forms.ModelChoiceField(
        required=False,
        queryset = Cobrador.objects.all(),
        widget=forms.Select(
           
            attrs={
                'class':'form-select',
            }
        )
    )
    nombre      = forms.CharField(
        required=False,
        min_length=2,
        max_length=255,
        widget=forms.TextInput(
            attrs={
                'class':"form-control",
                'placeholder':"add name"
            }
        )
    )
    codigo      = forms.IntegerField(
                                     widget=forms.TextInput(
            attrs={
                'class':"form-control",
                'placeholder':"Codigo"
            }
        )
                                     )
    N_cedula    = forms.CharField(
        required=False,
        min_length=2,
        max_length=255,
        widget=forms.TextInput(
            attrs={
                'class':"form-control",
                'placeholder':"add numero de cedula"
            }
        )
    )
    Comunidad   = forms.CharField(
        required=False,
        min_length=2,
        max_length=255,
        widget=forms.TextInput(
            attrs={
                'class':"form-control",
                'placeholder':"Comunidad"
            }
        )
    )
    Direccion   = forms.CharField(
        required=False,
        min_length=2,
        max_length=255,
        widget=forms.TextInput(
            attrs={
                'class':"form-control",
                'placeholder':"Descripcion"
            }
        )
    )
    
    update_at   = models.DateField()
    

   
    class Meta:
        model = Contribuyente
        fields= (
            "__all__"
        )'''