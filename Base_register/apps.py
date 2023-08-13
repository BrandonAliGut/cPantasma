from django.apps import AppConfig


class BaseRegisterConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Base_register'
