import paho.mqtt as mqtt
import paho.mqtt.client
import paho.mqtt.publish
from petfeeder.models import PetFeeder, Pet, FoodDispenserAction, UserRequestAction
from django.conf import settings
import json
import uuid
from multiprocessing.connection import Listener


# This class has two responsibilities:
#   1. Read from the pet feeders then write to the database
#   2. Read request from web server, send to pet feeder
        ######## TODO put in REST actions for UserRequestAction
class MqttReceiverClient:
    
    def __init__(self):
        print("You created a client!")

        self.client = mqtt.client.Client()
        self.client.on_message = self.on_message

        #print("Creating PetFeeder model...")
        #p = PetFeeder(
        #    serial_id="12345678",
        #    food_brand="brand1",
        #    food_servings=2,
        #    nutrition_calories=4,
        #    nutrition_serving_size=5
        #)
        #p.save()

    def __del__(self):
        self.client.disconnect()


    def on_message(self, client, userdata, message):
        ## client is the actual object client mqtt.Client
        #print("client: ", dir(client))
        print("userdata: ", userdata)
        self.handle_feeder_request(message)
        pass


    # Handles requests from the pet food feeder to update information
    def handle_feeder_request(self, message):
        #print(dir(message))
        print(message.payload)

        # pet info update
            # update in db

            # if chip ID updated, send on MQTT to feeder


        # pet feeder update
            # update in DB

            # if food brand or food mass 
        

        # dispenser action

    def start(self):
        self.client.connect(settings.MQTT_BROKER_ADDRESS)
        self.client.subscribe(settings.FEEDER_PULL_CHANNEL)
        while(True):
            self.client.loop()
        
        


# Sending functions
def publish(channel, payload):
    mqtt.publish.single(
        channel,
        payload=payload,
        qos=2,
        hostname=settings.MQTT_BROKER_ADDRESS,
        port=settings.MQTT_BROKER_PORT
    )


def push(feeder_id, data_dict):
    data_dict['request_id'] = str(uuid.uuid4())
    json_obj = json.dumps(data_dict)
    #print("WARNING: PUSH IS NOT ENABLED. ENABLE IN mqtt_utils.py")
    print(feeder_id)
    print(json_obj)
    publish(settings.FEEDER_PUSH_CHANNEL_ID.format(id=feeder_id), payload=json_obj)


def feeder_update_fields(serial_id, request_data):
    data = dict()
    data[settings.OP_FIELD] = settings.FEEDER_PUSH_FUNCTIONS["UPDATE"]
    data[settings.OPDATA_FIELD] = strip_data(PetFeeder, request_data)
    push(serial_id, data)

def feeder_sync(serial_id):
    data = dict()
    data[settings.OP_FIELD] = settings.FEEDER_PUSH_FUNCTIONS["SYNC"]
    feeders = PetFeeder.objects.filter(serial_id=serial_id)
    if len(feeders) != 1:
        print("ERROR: Found " + len(feeders) + " feeders with a serial id of " +
              serial_id)
        return
    feeder = feeders[0]
    data["chip_id"] = feeder.pet.chip_id
    data["setting_cup"] = feeder.setting_cup
    data["setting_interval"] = feeder.setting_interval

    push(serial_id, data)

def feeder_closure(serial_id, option):
    data = dict()
    data[settings.OP_FIELD] = settings.FEEDER_PUSH_FUNCTIONS["CLOSURE"]
    data[settings.OPDATA_FIELD] = dict()
    data[settings.OPDATA_FIELD]['option'] = option
    push(serial_id, data)

# Model functions
def strip_data(model, data):
    new_args = dict()
    if hasattr(model, 'MqttMeta') and hasattr(model.MqttMeta, 'allowed_fields'):
        for key in model.MqttMeta.allowed_fields:
            if key in data:
                new_args[key] = data[key]
    return new_args
