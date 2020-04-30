from django.utils import timezone

from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model= Employee
        fields= '__all__'
        read_only_fields=("created_at","updated_at")

    def create(self, validated_data):
        obj = super().create(validated_data)
        obj.created_at=timezone.now()
        obj.save()
        return obj

    def update(self, instance, validated_data):
        old_created_at=instance.created_at
        obj=super().update(instance,validated_data)
        obj.created_at=old_created_at
        obj.updated_at=timezone.now()
        obj.save()
        return obj


    def validate_name(self,value):
        if value=="Ahmad":
            raise serializers.ValidationError("you are blocked")
        else:
            return value
    def validate_age(self, value):
        if value <= 18:
            raise serializers.ValidationError("you are under 18")
        else:
            return value


