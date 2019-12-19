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

class GameListAPIView(ListAPIView):

    queryset = Game.objects.all()
    serializer_class = GameSerializer
    #def get_queryset()
    permission_classes = [IsAuthenticated]

    search_fields = ['first_name' , 'last_name' , 'father_name' , 'nat_code' , 'address__address']

    def get_queryset(self , *args , **kwargs):
        #queryset_list = super(GameListAPIView , self).get_queryset(*args , **kwargs)
        queryset_list = Game.objects.all()
        query = self.request.GET.get('q')
        if query:
            queryset_list = queryset_list.filter(
            Q(first_name__icontains = query)|
            Q(last_name__icontains = query)|
            Q(father_name__icontains = query)|
            #Q(address__address_id__icontains = query)|
            #Q(school__id__icontains = query)|
            Q(nat_code__icontains = query)
            #Q(theory_class__id = query)
            ).distinct()

        return queryset_list

class GameDetailAPIView(RetrieveAPIView):

    queryset = Game.objects.all()
    serializer_class =  GameSerializer
    lookup_field = 'nat_code'
    lookup_url_kwarg = 'nat_code'
    permission_classes = [IsOwnerOrReadOnly , IsAuthenticated]

class GameUpdateAPIView(UpdateAPIView):

    queryset = Game.objects.all()
    serializer_class =  GameCreateSerializer
    lookup_field = 'nat_code'
    lookup_url_kwarg = 'nat_code'
    permission_classes = [IsOwnerOrReadOnly]

    def perform_update(self , serializer):

        serializer.save(user = self.request.user)

class GameDeleteAPIView(DestroyAPIView):

    queryset = Game.objects.all()
    serializer_class =  GameSerializer
    lookup_field = 'nat_code'
    lookup_url_kwarg = 'nat_code'
    #def get_queryset()
    permission_classes = [IsOwnerOrReadOnly , IsAuthenticated]

class GameCreateAPIView(CreateAPIView):

    queryset = Game.objects.all()
    serializer_class = GameCreateSerializer
    permission_classes = [IsOwnerOrReadOnly , IsAuthenticated]