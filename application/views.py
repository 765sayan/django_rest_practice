from rest_framework.parsers import JSONParser
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from rest_framework.decorators import api_view, authentication_classes, permission_classes
import io
from django.http import JsonResponse
from . import models
from . import serializers
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated



# Create your views here.
# @csrf_exempt
# @authentication_classes([JWTAuthentication])


@api_view(['GET', 'POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def Authenticated(request):
    #The below ones are for class based views. For function based views we need to use decorators
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]
    employee_instance = models.Employee.objects.all()
    serialize = serializers.EmployeeSerializer(employee_instance, many=True)
    return JsonResponse(serialize.data, safe=False)
    # Res = {"Auth": "done"}
    # return JsonResponse(Res, safe=False)




@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def create(request):
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serialize = serializers.EmployeeSerializer(data = python_data)
        if serialize.is_valid():
            serialize.save()
            res = {"msg": "Employee Created"}
            return JsonResponse(res, safe=False)