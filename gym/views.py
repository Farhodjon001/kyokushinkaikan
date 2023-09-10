from django.shortcuts import render
from .models import GymModel
from .serializers import GymSerializers
from rest_framework import generics

# Create your views here.

class GYMListApieview(generics.ListAPIView):
    queryset = GymModel.objects.all()
    serializer_class = GymSerializers

class GYMUpdateApieview(generics.UpdateAPIView):
    queryset = GymModel.objects.all()
    serializer_class = GymSerializers

class GYMDeleteApieview(generics.DestroyAPIView):
    queryset = GymModel.objects.all()
    serializer_class = GymSerializers

class GYMCreateApieview(generics.CreateAPIView):
    queryset = GymModel.objects.all()
    serializer_class = GymSerializers

class GYMDetailsApieview(generics.RetrieveAPIView):
    queryset = GymModel.objects.all()
    serializer_class = GymSerializers
