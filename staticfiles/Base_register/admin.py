from django.contrib import admin
from .models import *
''''''
# Register your models here.
admin.site.register(Cobrador)
admin.site.register(Contribuyente)
admin.site.register(Years)
admin.site.register(Months)



admin.site.register(UpdateMonthsContry)


admin.site.register(Empresa)


admin.site.register(CuentasPagos)


admin.site.register(PagoCuenta)