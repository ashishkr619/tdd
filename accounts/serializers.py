from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ['id','email','full_name','phone','pincode']


class UserRegisterSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ['id','email','password','full_name','phone','pincode']
    extra_kwargs = {'password':{'write_only':True},}