from django.shortcuts import render

# Create your views here.
from rest_framework import status, viewsets, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from car.models import Person, Car

from car.serializers import PersonSerializer, CarSerializer, CarReadSerializer


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




@permission_classes((AllowAny,))
class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    http_method_names = ['get','post','put','delete']

    search_fields=('name',)
    ordering_fields= '__all__'

    def list(self, request, *args, **kwargs):
        run=super().list(request, *args, **kwargs)
        objects=self.get_queryset()
        i=0
        for s in objects:
            i+=1
            print(f"___number={i}___{s.name}")
        return run

    def create(self, request, *args, **kwargs):
        run=super().create(request, *args, **kwargs)
        print(f"___new person is created___")
        return run

    def update(self, request, *args, **kwargs):
        run=super().update(request, *args, **kwargs)
        object=self.get_object()
        print(f"___new person with name : {object.name} is updated___")
        return run

    def retrieve(self, request, *args, **kwargs):
        run=super().retrieve(request,*args,**kwargs)
        object=self.get_object()
        print(f"___ retrieve : {object.name} data___")
        return run

    def destroy(self, request, *args, **kwargs):
        object = self.get_object()
        run=super().destroy(request,*args,**kwargs)
        print(f"___{object.name} deleted successfully ___")
        return run


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    http_method_names = ['get','post', 'put', 'delete']

    def get_serializer_class(self):
        if self.request.method not in permissions.SAFE_METHODS:
            return CarSerializer
        else:
            return CarReadSerializer