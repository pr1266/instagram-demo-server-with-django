from .models import *
from rest_framework.serializers import ModelSerializer , SerializerMethodField , CharField , ValidationError , StringRelatedField, PrimaryKeyRelatedField
from django.db.models import Q

class CustomUserSerializer(ModelSerializer):

    class Meta:
        model  = CustomUser 
        fields = '__all__'

class CitySerializer(ModelSerializer):

    class Meta:
        model  = City 
        fields = '__all__'

class AddressSerializer(ModelSerializer):

    class Meta:
        model  = Address 
        fields = '__all__'

class CustomerSerializer(ModelSerializer):

    class Meta:
        model  = Customer 
        fields = '__all__'

class PlatformSerializer(ModelSerializer):

    class Meta:
        model  = Platform
        fields = '__all__'

class GameCategorySerializer(ModelSerializer):

    class Meta:
        model  = G_CATEGORY 
        fields = '__all__'