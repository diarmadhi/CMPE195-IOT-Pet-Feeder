from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from petfeeder.models import PetFeeder, PetFood, Pet, FoodDispenserAction, UserRequestAction
from petfeeder.serializers import *
from petfeeder.permissions import IsOwner
from petfeeder import mqtt_utils
import datetime
import json

from rest_framework import permissions

class CustomObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super(CustomObtainAuthToken, self).post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        return Response({'token': token.key, 'id': token.user_id})


class CreateUserView(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserSerializer

# View for read, create operations
class PetFeederViewSet(viewsets.ModelViewSet):
    serializer_class = PetFeederSerializer
    permission_classes = (IsOwner, permissions.IsAuthenticated,)

    def dispatch(self, request, *args, **kwargs):
        import pprint
        #pprint.pprint(vars(request))
        pprint.pprint(request.content_type)
        pprint.pprint(request.body)
        return super().dispatch(request, *args, **kwargs)

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
            #mqtt_utils.feeder_update_fields(serial_id, request.data)
            mqtt_utils.feeder_sync(serial_id)

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

    def dispatch(self, request, *args, **kwargs):
        #import pprint
        #pprint.pprint(vars(request))
        #print(request.content_type)
        #print(request.body)
        return super().dispatch(request, *args, **kwargs)
        
    #def create(self, validated_data):
    #    print(validated_data.data)
    #    return super().create(validated_data)


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

@api_view(['GET'])
def PetConsumptionSummary(request):
    user = request.user
    if not user.is_authenticated:
        return Response({"message": "User not authenticated"});
    length = request.query_params.get('length')
    if length != None and length.isdigit():
        length = int(length)
    else:
        length = 14
    
    pet = Pet.objects.filter(id=request.query_params.get('pet'))
    if len(pet) != 1:
        return Response({"message": "Pet not found"})
    pet = pet[0]
    if not pet.user == user:
        return Response({"message": "Pet does not belong to user"})
    consumption = PetConsumptionAction.objects.filter(pet=pet)

    # max date based on latest feeding
    '''
    if len(consumption) > 0:
        max_date = consumption[0].time.date()
    for action in consumption:
        max_date = max(action.time.date(), max_date)
    max_date = max_date + datetime.timedelta(days=1)
    '''

    max_date = datetime.datetime.now()

    consumption_map = {}
    for i in range(length):
        consumption_map[max_date - datetime.timedelta(days=i)] = 0

    for action in consumption:
        date = action.time.date()
        if date not in consumption_map:
            continue
            #consumption_map[date] = 0

        food = action.food
        # food.density = mass per cup
        calories = 0
        if food is not None:
            calories = action.mass/food.density*food.calories_serving
        consumption_map[date] += calories

    return JsonResponse([{str(x): y} for x,y in consumption_map.items()], safe=False)

