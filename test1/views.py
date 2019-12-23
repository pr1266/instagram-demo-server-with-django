from rest_framework.generics import ListAPIView , RetrieveAPIView , CreateAPIView , UpdateAPIView , DestroyAPIView
from .models import *
from .serializer import *
from django.core import serializers
from django.db.models import Q
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import permission_classes , api_view
from django.db.models import F
from django.http import JsonResponse , HttpResponse
from rest_framework.permissions import(
    AllowAny ,
    IsAuthenticated ,
    IsAdminUser ,
    IsAuthenticatedOrReadOnly ,
)
from django.views.generic import View
from rest_framework.status import HTTP_200_OK , HTTP_400_BAD_REQUEST
from rest_framework.filters import(
    SearchFilter ,
    OrderingFilter ,
)
from django.db.models import Count, Case, When, IntegerField
import datetime
import time
import json

#! Game :

class GameListAPIView(ListAPIView):

    queryset = Game.objects.all()
    serializer_class = GameSerializer
    permission_classes = [IsAuthenticated]

    search_fields = '__all__'

    def get_queryset(self , *args , **kwargs):
        queryset_list = Game.objects.all()
        query = self.request.GET.get('q')
        if query:
            queryset_list = queryset_list.filter(
            Q(name__icontains = query)|
            Q(id__icontains = query)|
            Q(gamePlt__name__icontains = query)|
            Q(gameCat__name__icontains = query)
            ).distinct()

        return queryset_list

class GameDetailAPIView(RetrieveAPIView):

    queryset = Game.objects.all()
    serializer_class =  GameSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'id'
    permission_classes = [IsAuthenticated,]

class GameUpdateAPIView(UpdateAPIView):

    queryset = Game.objects.all()
    serializer_class =  GameSerializer
    lookup_field = 'nat_code'
    lookup_url_kwarg = 'nat_code'
    permission_classes = []
    def perform_update(self , serializer):

        serializer.save(user = self.request.user)

class GameDeleteAPIView(DestroyAPIView):

    queryset = Game.objects.all()
    serializer_class =  GameSerializer
    lookup_field = 'nat_code'
    lookup_url_kwarg = 'nat_code'
    #def get_queryset()
    permission_classes = [IsAuthenticated,]

class GameCreateAPIView(CreateAPIView):

    queryset = Game.objects.all()
    serializer_class = GameSerializer
    permission_classes = [IsAuthenticated,]

#! accessories :

class AccessoryDetailAPIView(RetrieveAPIView):

    queryset = Accessory.objects.all()
    serializer_class = AccessorySerializer
    permission_classes = [IsAuthenticated,]
    search_fields = ['id' , 'name' , 'accessoryCat__name', 'accessoryPlt_name']
    lookup_field = 'id'
    lookup_url_kwarg = 'id'

class AccessoryCreateAPIView(CreateAPIView):

    queryset = Accessory.objects.all()
    serializer_class = AccessorySerializer
    permission_classes = [IsAuthenticated,]

class AccessoryDeleteAPIView(DestroyAPIView):

    queryset = Accessory.objects.all()
    serializer_class = AccessorySerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'id'
    permission_classes = [IsAuthenticated,]

    def delete(self , request , id):

        obj = Accessory.objects.get(pk = id)
        obj.delete()
        print("salam")
        return Response(status = HTTP_200_OK)

class AccessoryUpdateAPIView(UpdateAPIView):

    queryset = Accessory.objects.all()
    serializer_class = AccessorySerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'id'
    permission_classes = [IsAuthenticated,]

#! GAME ORDERS :
class GameOrderListAPIView(ListAPIView):

    queryset = GameOrder.objects.all()
    serializer_class = GameOrderSerializer
    permission_classes = [IsAuthenticated]

    search_fields = '__all__'

    def get_queryset(self , *args , **kwargs):
        queryset_list = GameOrder.objects.all()
        query = self.request.GET.get('q')
        if query:
            queryset_list = queryset_list.filter(
            Q(name__icontains = query)|
            Q(id__icontains = query)|
            Q(gamePlt__name__icontains = query)|
            Q(gameCat__name__icontains = query)
            ).distinct()

        return queryset_list

class GameOrderDetailAPIView(RetrieveAPIView):

    queryset = GameOrder.objects.all()
    serializer_class =  GameOrderSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'id'
    permission_classes = [IsAuthenticated,]

class GameOrderUpdateAPIView(UpdateAPIView):

    queryset = GameOrder.objects.all()
    serializer_class =  GameOrderSerializer
    lookup_field = 'nat_code'
    lookup_url_kwarg = 'nat_code'
    permission_classes = []
    def perform_update(self , serializer):

        serializer.save(user = self.request.user)

class GameOrderDeleteAPIView(DestroyAPIView):

    queryset = GameOrder.objects.all()
    serializer_class =  GameOrderSerializer
    lookup_field = 'nat_code'
    lookup_url_kwarg = 'nat_code'
    permission_classes = [IsAuthenticated,]

class GameOrderCreateAPIView(CreateAPIView):

    queryset = GameOrder.objects.all()
    serializer_class = GameOrderSerializer
    permission_classes = [IsAuthenticated,]

#! GAMES : 
#! get games by platform
@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def GetPltGames(request):

    plt = request.data['plt']
    obj = Game.objects.filter(gamePlt__name = plt)

    ser_obj = GameSerializer(obj, many = True)

    return Response(ser_obj.data)

#! games by category
@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def GetCatGames(request):

    plt = request.data['plt']
    obj = Game.objects.filter(gameCat__name = plt)

    ser_obj = GameSerializer(obj, many = True)

    return Response(ser_obj.data)

#! get games by platform
@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def GetPltAccessories(request):

    plt = request.data['plt']
    obj = Accessory.objects.filter(accessoryPlt__name = plt)

    ser_obj = AccessorySerializer(obj, many = True)

    return Response(ser_obj.data)


#! ACCESSORIES
#! accessory by category
@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def GetCatAccessories(request):

    plt = request.data['plt']
    obj = Accessory.objects.filter(gameCat__name = plt)

    ser_obj = AccessorySerializer(obj, many = True)

    return Response(ser_obj.data)



#! GAME ORDERS : 



#! GAME DELIVERIES :
