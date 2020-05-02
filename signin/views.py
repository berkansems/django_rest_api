from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from signin.permisions import IsOwner
from signin.serializers import UserSerializer


@api_view(['post'])
@permission_classes((AllowAny,))
def create_user(request):
    ser=UserSerializer(data=request.data)
    if ser.is_valid():
        ser.save()
        return Response(ser.data,status=status.HTTP_201_CREATED)
    else:
        return Response(status.HTTP_404_NOT_FOUND)

@api_view(['get'])
@permission_classes((IsAuthenticated,IsOwner))
def profile(request):
    try:
        user=User.objects.get(username=request.query_params['username'])
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    ser=UserSerializer(user)
    return Response(ser.data)

