from django.shortcuts import render
from .serializers import ProfileSerializer, HeartUserSerializer, RestTestSerializer
from .models import HeartUser, RestTest
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

@api_view(['GET','POST'])
@permission_classes((IsAuthenticated,))
def hello(request):
    users = HeartUser.objects.all()
    serializer = HeartUserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def resttest(request):
    print(request.data['name'])
    data = {"user":request.user.id, "file":request.data['file']}
    serializer = RestTestSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
    else:
        print(serializer.errors)
        return Response(JSONRenderer().render({"error":"error in saving serializer"}))
    
    return Response(JSONRenderer().render({"success":"success is sweet"}))