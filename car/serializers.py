from rest_framework import serializers, viewsets

from car.models import Person, Car


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields='__all__'

class CarSerializer(serializers.ModelSerializer):

    class Meta:
        model = Car
        fields='__all__'
        #depth=1

class CarReadSerializer(serializers.ModelSerializer):
    person=PersonSerializer()# or just type depth=1
    class Meta:
        model = Car
        fields='__all__'
        #depth=1
