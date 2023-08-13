from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings

from .view_index import index, Admin_page_home,IndexRegister,contribuyente,Estado_Contribuyente,trabajo_type_pagos
#index home
urlpatterns = [
    path(" ",index, name="home"),
    path("Home_page/", Admin_page_home.as_view(), name="home_grupo"),
    path("Home_Register/", IndexRegister, name="home_admin"),
    path("SuperAdmin", superAdmin, name="admin_contabilidad"),
    path("add_contribu/<str:typeaction>/<str:pk>", contribuyente, name="add_contribuyente"),
    path("EstadoContri", Estado_Contribuyente, name="EstadoContri"),
    path("add_trabajos/<str:typeaction>/<str:pk>/<str:add>", trabajo_type_pagos, name="add_trabajo"),
    
    
    

    
]


urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)