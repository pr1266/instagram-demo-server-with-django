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
        model  = G_Category
        fields = '__all__'

class GameSerializer(ModelSerializer):

    class Meta:
        model  = Game
        fields = '__all__'

class GameOrderSerializer(ModelSerializer):

    class Meta:
        model  = GameOrder 
        fields = '__all__'

class GameDeliverySerializer(ModelSerializer):

    class Meta:
        model  = GameDelivery 
        fields = '__all__'

class AccessoryCategorySerializer(ModelSerializer):

    class Meta:
        model  = A_Category 
        fields = '__all__'

class AccessorySerializer(ModelSerializer):

    class Meta:
        model  = Accessory
        fields = '__all__'

class AccessoryOrderSerializer(ModelSerializer):

    class Meta:
        model  = AccessoryOrder
        fields = '__all__'

class AccessoryDeliverySerializer(ModelSerializer):

    class Meta:
        model  = AccessoryDelivery
        fields = '__all__'
