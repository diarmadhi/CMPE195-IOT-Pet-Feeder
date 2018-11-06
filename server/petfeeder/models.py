from django.contrib.auth.models import User
from django.conf import settings
from django.dispatch import receiver
from django.db import models
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

def generate_tokens():
    for user in User.objects.all():
        Token.objects.get_or_create(user=user)
    


# Entities
class PetFeeder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    serial_id = models.CharField(unique=True, max_length=settings.UUID_LENGTH)
    food = models.ForeignKey('PetFood', on_delete=models.SET_NULL, null=True)
    setting_cup = models.PositiveIntegerField(default=0)
    setting_interval = models.PositiveIntegerField(default=0) # stored in minutes, 0 is off
    setting_closure = models.BooleanField(default=False)
    pet = models.OneToOneField('Pet', on_delete=models.SET_NULL, null=True)

    class MqttMeta:
        allowed_fields = ['serial_id', 'setting_cup', 'setting_interval', 'setting_closure']


class Pet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    chip_id = models.CharField(blank=False, max_length=settings.PET_RFID_LENGTH)
    pet_type = models.CharField(blank=True, default='', max_length=settings.PET_TYPE_LENGTH)
    pet_breed = models.CharField(blank=True, default='', max_length=settings.PET_BREED_LENGTH)
    name = models.CharField(blank=True, default='', max_length=settings.NAME_LENGTH)
    birthday = models.DateField(blank=True, default=None)


class PetFood(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=settings.FOOD_BRAND_LENGTH)
    calories_serving = models.PositiveIntegerField(default=0)
    cups_serving = models.FloatField(default=0)
    density = models.FloatField(default=0)


class Profile(User):
     user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)


# Relationships
class FoodDispenserAction(models.Model):
    feeder = models.ForeignKey('PetFeeder', on_delete=models.SET_NULL, null=True)
    food = models.ForeignKey('PetFood', on_delete=models.CASCADE)
    time = models.DateTimeField()
    cups = models.FloatField(default=0)
    command = models.PositiveIntegerField(default=2)


class UserRequestAction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    feeder = models.ForeignKey('PetFeeder', on_delete=models.SET_NULL, null=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(blank=True, default=None)
    request_type = models.IntegerField()
    status = models.IntegerField()


class PetConsumptionAction(models.Model):
    pet = models.ForeignKey('Pet', on_delete=models.CASCADE)
    food = models.ForeignKey('PetFood', on_delete=models.CASCADE)
    time = models.DateTimeField()
    mass = models.PositiveIntegerField(default=0)



