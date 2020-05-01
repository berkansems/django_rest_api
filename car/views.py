from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from car.models import Person, Car

from car.serializers import PersonSerializer, CarSerializer


@api_view(['POST','GET'])
def personView(request):
   if request.method == 'POST':

       ser=PersonSerializer(data=request.data)
       if ser.is_valid():
           ser.save()
           return Response(ser.data,status=status.HTTP_200_OK)
       else:
           return Response(ser.errors,status=status.HTTP_404_NOT_FOUND)

   elif request.method == 'GET':
       persons=Person.objects.all()
       ser=PersonSerializer(persons,many=True)

       return Response(ser.data,status=status.HTTP_200_OK)

@api_view(['POST','GET'])
def carView(request):
    if request.method == "POST":
        ser=CarSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data,status=status.HTTP_201_CREATED)
        else:
            return Response(ser.errors,status=status.HTTP_400_BAD_REQUEST)
    if request.method == "GET":
        cars=Car.objects.all()
        ser=CarSerializer(cars,many=True)
        return Response(ser.data,status=status.HTTP_200_OK)
