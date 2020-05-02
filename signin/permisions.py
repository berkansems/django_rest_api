from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework.response import Response


class IsOwner(permissions.BasePermission):
    def has_permission(self, request, view):
        try:
            user=User.objects.get(username=request.query_params['username'])
        except:
            return False
        if request.user.is_superuser:
            return True
        if not request.user == user:
            return False
        else:
            return True




 #   def has_permission(self, request, view):
 #       try:
 #           user = User.objects.get(username=request.query_params['username'])
 #       except:
 #           return False
 #       if request.user.is_superuser:
 #           return True
 #       if not request.user == user:
 #           return False
 #       else:
 #           return True
#