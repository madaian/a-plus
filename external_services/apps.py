from django.apps import AppConfig


class Config(AppConfig):
    name = 'external_services'
    verbose_name = 'ExternalServices'

    def ready(self):
        # Load our receivers
        # This is important as receiver hooks are not connected otherwise.
        from . import receivers  # NOQA
