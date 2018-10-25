from rest_framework import serializers
from django.contrib.auth.models import User
from petfeeder.models import PetFeeder, Pet, PetFood, Profile, FoodDispenserAction, UserRequestAction, PetConsumptionAction

class PetFeederSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetFeeder
        fields = '__all__'


class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = '__all__'


class PetFoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetFood
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'password')

    password = serializers.CharField(write_only=True)
    def create(self, validated_data):
        user = User.objects.create(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user



class FoodDispenserActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodDispenserAction
        fields = '__all__'


class UserRequestActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRequestAction
        fields = '__all__'


class PetConsumptionActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetConsumptionAction
        fields = '__all__'
