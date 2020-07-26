from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .serializers import UserSerializer,UserRegisterSerializer
from rest_framework.permissions import AllowAny

User = get_user_model()

class RegisterAPIView(APIView):
  serializer_class = UserRegisterSerializer
  permission_classes = (AllowAny,)
  def post(self,request):
    try:
      email = request.data["email"]
      password = request.data["password"]
      full_name = request.data["full_name"]
      phone = request.data["phone"]
      pincode = request.data["pincode"]
      user = User.objects.filter(email=email)
      if user:
        return Response({message:"User already exists"},status=status.HTTP_409_CONFLICT)
      else:
        user = User.objects.create_user(email=email,password=password,full_name=full_name,phone=phone,pincode=pincode)
        user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    except:
      return Response(status=status.HTTP_400_BAD_REQUEST)
   
