from django.shortcuts import render

# views contabilidad.
def superAdmin(request):
    content = {
            "data":"hola"
        }
    return render(request, "contabilidad/contabilidad_bace.html", content)