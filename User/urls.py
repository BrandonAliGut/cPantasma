from django.urls import path
from User import views

urlpatterns = [
    path("createuser/", views.Register, name="register" ),
    path("login/", views.Inicio_de_sesion, name="login" ),
    path("logout/", views.Logout.as_view(), name="logout" )
]