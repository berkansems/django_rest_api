from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Employee
from .serializers import EmployeeSerializer

@api_view(['POST'])
def post_employe(request):
    data ={
        'name':request.data['name'],
        'age':request.data['age'],
        'salary':request.data['salary'],
        'post':request.data['post']
    }

    ser= EmployeeSerializer(data=data)
    print(ser)
    if ser.is_valid():
        ser.save()
        return Response(ser.data,status=status.HTTP_201_CREATED )
    else:
        return Response(ser.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_employees(request):
    employees=Employee.objects.all()
    print(employees)
    ser=EmployeeSerializer(employees,many=True)
    return Response(ser.data,status=status.HTTP_200_OK)

@api_view(['GET','PUT','DELETE'])
def select(request,pk):
    try:
        employee = Employee.objects.get(id=pk)
        ser = EmployeeSerializer(employee)
        if request.method == 'GET':
            return Response(ser.data,status=status.HTTP_200_OK)
        elif request.method == 'PUT':
            ser=EmployeeSerializer(employee,data=request.data)
            if ser.is_valid():
                ser.save()
                return Response(ser.data, status=status.HTTP_200_OK)
        elif request.method == 'DELETE':
            employee.delete()
            return Response({f"employee with this id {pk} deleted"})
    except:
        return Response({"message":"not found"},status=status.HTTP_400_BAD_REQUEST)
#   if ser.is_valid():
#       if request.method == 'PUT':
#           ser=EmployeeSerializer(data=data)
#           if ser.is_valid():
#               ser.save()
#               return Response(ser.data,status=status.HTTP_201_CREATED)
#       elif request.method == 'GET':
#           pass
#       elif request.method == 'DELETE':
#           pass
#       else:
#           return Response(ser.errors,status=status.HTTP_400_BAD_REQUEST)

#   else:
#       return Response(ser.errors,status=status.HTTP_400_BAD_REQUEST)


#to run query params you should write link like this: 127.0.0.1:8000/search_employee?name=Ali
@api_view(['GET'])
def search_employee(request):
    employees=Employee.objects.filter(name=request.query_params['name'])

    if employees:
        ser = EmployeeSerializer(employees,many=True)
        return Response(ser.data)

    else:
        return Response(status=status.HTTP_404_NOT_FOUND)