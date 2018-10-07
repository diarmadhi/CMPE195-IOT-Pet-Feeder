from django.core.management.base import BaseCommand
from petfeeder.mqtt_utils import MqttReceiverClient

class Command(BaseCommand):
    help = 'Start the MQTT instance(s)'

    def add_arguments(self, parser):
        parser.add_argument( '-n', dest='number', required=False, default=1)

    def handle(self, *args, **options):
        client = MqttReceiverClient()
        client.start()
