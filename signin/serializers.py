from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ('username','password', 'first_name','email')

    def create(self, validated_data):
        user=super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user