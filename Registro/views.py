from django.shortcuts import render, redirect
def superAdmin(request):
    content = {
            "data":"hola"
        }
    return render(request, "contabilidad/contabilidad_bace.html", content)