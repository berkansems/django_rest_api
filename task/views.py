from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CalcSerializer

@api_view()
def hello_world(request):
    return Response({"message":"Hello, World"})


@api_view(['POST','GET'])
def hello(request):
    if request.method == "GET":
        return Response({"message": "get method"})
    elif request.method == "POST":
        return Response({"message": "Hello {}".format(request.data["name"])})



@api_view(['post'])
def calculator(request):

    try:
        num1= request.data['num1']
        num2= request.data['num2']
        opr= request.data['opr']
    except:
        return Response({"message":"please inter num1 num2 opr correctly"},
                        status=status.HTTP_400_BAD_REQUEST)
    else:
        if isinstance(num1,int) and isinstance(num2,int):
            if opr == "plus":
                result=num1+num2
                return Response({f"plus of two number is: {result}"},status=status.HTTP_200_OK)
            elif opr == "min":
                result=num1-num2
                return Response({f"minus of two number is: {result}"},status=status.HTTP_200_OK)
            elif opr =="mul":
                result=num1*num2
                return Response({f"multiple of two numbers are: {result}"},status=status.HTTP_200_OK)
            else:
                return Response({"message": "please select correct opr"})
        else:
            return Response({"message":"num1 or num2 is not integer"},status=status.HTTP_400_BAD_REQUEST)



@api_view(['POST'])
def newcalculator(request):

    ser = CalcSerializer(data=request.data)
    if ser.is_valid():
        num1= ser.data['num1']
        num2= ser.data['num2']
        opr= ser.data['opr']

        if opr == "add":
            return Response ({"add result is":num1+num2},status=status.HTTP_200_OK)

        elif opr == "div":
            return Response ({"resut of deviding is":num1/num2},status=status.HTTP_200_OK)

    else:
        return Response(ser.errors)
