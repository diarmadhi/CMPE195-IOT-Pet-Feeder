from django.shortcuts import render
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from petfeeder.models import PetFeeder, PetFood, Pet, FoodDispenserAction, UserRequestAction
from petfeeder.serializers import *
from petfeeder.permissions import IsOwner
from petfeeder import mqtt_utils
import json

from rest_framework import permissions

# View for read, create operations
class PetFeederViewSet(viewsets.ModelViewSet):
    serializer_class = PetFeederSerializer
    permission_classes = (IsOwner, permissions.IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return PetFeeder.objects.filter(user=user)
        if user.is_superuser:
            return PetFeeder.objects.all()
        return PetFeeder.objects.none()

    def update(self, request, *args, **kwargs):
        # generate MQTT request
        #~print(request.data)
        #~print(args)
        #~print(kwargs)
        feeder_query = PetFeeder.objects.filter(id=kwargs['pk'])
        if feeder_query:
            serial_id = feeder_query[0].serial_id
            mqtt_utils.feeder_update_fields(serial_id, request.data)

        return super().update(request, *args, **kwargs)


class PetViewSet(viewsets.ModelViewSet):
    permission_classes = (IsOwner, permissions.IsAuthenticated, )
    serializer_class = PetSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Pet.objects.filter(user=user)
        if user.is_superuser:
            return Pet.objects.all()
        return Pet.objects.none()


class PetFoodViewSet(viewsets.ModelViewSet):
    serializer_class = PetFoodSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return PetFood.objects.filter(user=user)
        if user.is_superuser:
            return PetFood.objects.all()
        return PetFood.objects.none()


class FoodDispenserActionViewSet(viewsets.ModelViewSet):
    serializer_class = FoodDispenserActionSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            feeders = PetFeeder.objects.filter(user=user)
            return FoodDispenserAction.objects.filter(feeder__in=feeders)
        if user.is_superuser:
            return FoodDispenserAction.objects.all()
        return FoodDispenserAction.objects.none()


class UserRequestActionViewSet(viewsets.ModelViewSet):
    serializer_class = UserRequestActionSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return UserRequestAction.objects.filter(user=user)
        if user.is_superuser:
            return UserRequestAction.objects.all()
        return UserRequestAction.objects.none()


class PetConsumptionActionViewSet(viewsets.ModelViewSet):
    serializer_class = PetConsumptionActionSerializer

    def get_queryset(self):
        user = self.request.user
        pets = Pet.objects.filter(user=user)
        if user.is_authenticated:
            return PetConsumptionAction.objects.filter(pet__in=pets)
        if user.is_superuser:
            return PetConsumptionAction.objects.all()
        return PetConsumptionAction.objects.none()
