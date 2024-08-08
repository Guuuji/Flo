from django.apps import AppConfig


class WwwConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'www'

    def ready(self):
        from .scheduler import start_scheduler
        start_scheduler()
