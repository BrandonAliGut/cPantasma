from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.contrib import messages
from django.views.generic import CreateView, ListView, UpdateView
from django.contrib.auth.mixins import PermissionRequiredMixin
from .forms import *
from datetime import date
from Base_register.models import *
from .sumary import Control


class Admin_page_home(PermissionRequiredMixin,ListView):
    permission_required= (
        'Api_grup_all.view_grupoanimals'
    )
    template_name= "page_all/lis_groups.html"


    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            try: 
                """content_type = ContentType.objects.get_for_model(GrupoAnimals)
                permission_group = Permission.objects.filter(content_type =content_type)
                print( [perm.codename for perm in permission_group])"""
                
                return render(request, "page_all/lis_groups.html")
            except:
                messages.success(request,'Error: la ruta no existe ')
                return redirect('home')
        return redirect('home')
    
def index(request):
    content = {
        "data":"hola"
    }
    return render(request, "index_tem/index.html", content)


def trabajo_type_pagos(request, typeaction="", pk=str(), add = "1"):
    
    
    sumary= Control(request)
    empresa =  request.GET.get('nombre_empresa') 
    direccion = request.GET.get('direccion') 
    print(empresa )
    print(direccion)
    actionudateadd = typeaction
    data = {
        "id":pk,
        "cuentas":CuentasPagos.objects.all(),
        "empresa": empresa,
        'direccion': direccion
        }


    if actionudateadd == "add":
        
        
        if add != 'None':
            sumary.additems()
        
        return( redirect('add_trabajo', 'contryempre', pk, None))
        
    
    
    if request.method == "POST":
        __model_at = Contribuyente.objects.get(pk = int(pk))
        print("si")
        data = {
        "id":pk,
        "cuentas":CuentasPagos.objects.all()
        }
        
        Empresa_pagos = None
        empresa =  request.GET.get('nombre_empresa') 
        direccion = request.GET.get('direccion') 
        if empresa != "":
            Empresa_pagos=Empresa(
                name_empresa = empresa,
                Direcion = direccion,
            )
            Empresa_pagos.save()
        
        if "sumary" in request.session.keys():
            for key, value in request.session["sumary"].items():
                if key != 'id':
                    conbox = request.POST.get(str(value["controlfor"]))
                    inputext = request.POST.get(str(value["control"]))
                    if conbox != "" or inputext != "":
                        
                        class_model = PagoCuenta(
                            empresa = Empresa_pagos,
                            contribuyente   = __model_at,
                            cuenta_pago     = CuentasPagos.objects.get(pk = int(conbox)),
                            cantidad        = inputext,
                        )
                        class_model.save()
                        
                        
                        
        sumary.deleteseccion()
                    
        return render(request, "IndexRegister/Typo_empresa.html", data)

    
    
    if actionudateadd == 'update':
        pass
    if actionudateadd == 'contryempre':
        return render(request, "IndexRegister/Typo_empresa.html",data)

    return render(request, "IndexRegister/Typo_empresa.html")




def IndexRegister(request):
    from django.db.models import Q
    search_table = request.GET.get("buscar_table")
    Contrybu=Contribuyente.objects.all().order_by('nombre')
    if search_table:
        Contrybu = Contribuyente.objects.filter(
            Q(nombre__icontains= search_table)
            
             
        ).distinct()
    
    if request.method == "GET":
        pass
    content = {
        "contribuyente": Contrybu
    }
    
    
    return render(request, "IndexRegister/ViewContribuyente.html", content)


def contribuyente(request, typeaction="add", pk=str()):
    
        
    actionudateadd = typeaction
    dataupdate = None
    
        
    __id = None
    __cobrador = int()
    __nombre = str()
    __codigo = int()
    __NCedula = str()
    __comunidad = str()
    __direccion = str()
    
    cobrador = Cobrador.objects.all()
    data = {
        "cobrador": Cobrador.objects.all(),
        "id":__id
        }
    ''''''
    
    
    
    if not __codigo:
        __codigo = None
    else: 
        __codigo = int(__codigo)
        
    if not __id:
        try:
            __id=int(__cobrador)
            
        except:
            __id= 0
            
    __cobrador = request.POST.get('cobrador')

    if not __cobrador:
        modelsc = None
    elif int(__cobrador) == 0:
        modelsc = None
    else:
        modelsc= Cobrador.objects.get(id= __cobrador)
            
    
        
    def start(request, data):
        return render(request, "IndexRegister/add_Contribuyente.html",data)
    
    def Apellido(I=str(), element=int()):
        if not I:
            return
        if  element >=1:
            print(element)
            if not element <= 1:
                if element >= 4:
                    apellidoInicial = I[-2]
                    
                    print(element)
                    print(apellidoInicial)
                elif element <= 3:
                    print(element)
                    apellidoInicial = I[-1]
                    print(apellidoInicial)
                else:
                    apellidoInicial = I[2]
            else:
                messages.success(request, '_!el campo nombre no puede tener un solo dato, agregar apellido completo y nombre')
                return 
            
        
        if apellidoInicial[:2] == "CH":
            Abc =  apellidoInicial[:2]
        else:
            Abc = apellidoInicial[0]
        return Abc
        
        """odername=Ordering(
                contryUnique= modelsc,
                type_abs =Abc,
                primer_apellido = apellidoInicial,
                complete_name = __nombre
             
            )"""
        

    __id = request.POST.get('ID')
    __nombre = request.POST.get('nombre')
    
    __codigo = request.POST.get('codigo')
    if __codigo != int():
        __codigo = None
   
    __NCedula = request.POST.get('NCedula')
    __comunidad = request.POST.get('Comunidad')
    __direccion = request.POST.get('Direccion')
    
    if __nombre:
        I=__nombre.split()    
        element= int(len(set(I)))
        Apellido(I,element)
        
    if not __nombre:
        messages.success(request, 'La referecia no es correcta (nombre y cobrador) no pueden estar bacios ')
    
        
    
    if actionudateadd == "add":
        if request.method == "POST":
            
            models_contry=Contribuyente(
                register_for=modelsc,
                nombre      = __nombre,
                codigo      = __codigo,
                N_cedula    = __NCedula,
                Comunidad   = __comunidad,
                Direccion   = __direccion,
                update_at   = date.today()
            )
            models_contry.save()
            
            return (redirect('add_contribuyente', 'add', 'new'))
        return render(request, "IndexRegister/add_Contribuyente.html",data)

    if actionudateadd == 'update':
        model_at = Contribuyente.objects.get(pk = int(pk))
        if request.method == "GET":
            if pk != "new":
                try: 
                    id_cobrador = model_at.register_for.pk
                except:
                    id_cobrador= None
                
                data = {
                        "cobrador": Cobrador.objects.all(),
                        "cbuyen": model_at,
                        "ID": id_cobrador,
                        
                    }
                return render(request, "IndexRegister/add_Contribuyente.html",data)
        if request.method == "POST":
            
            model_contryUpdate = Contribuyente.objects.filter(pk= int(pk)).update(
                register_for=modelsc,
                nombre      = __nombre,
                codigo      = __codigo,
                N_cedula    = __NCedula,
                Comunidad   = __comunidad,
                Direccion   = __direccion,
                update_at   = date.today()
            )
            
            return (redirect('add_contribuyente', 'update', pk))


def Estado_Contribuyente(request):
    return render(request, "IndexRegister/Estado_C.html")

def superAdmin(request):
    content = {
            "data":"hola"
        }
    return render(request, "contabilidad/contabilidad_bace.html", content)