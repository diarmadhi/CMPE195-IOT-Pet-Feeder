from django.apps import AppConfig


class PetfeederConfig(AppConfig):
    name = 'petfeeder'

    def ready(self):
        from petfeeder.models import generate_tokens
        generate_tokens()
