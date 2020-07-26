from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from django.shortcuts import reverse
from ..serializers import UserSerializer
from rest_framework import status

User = get_user_model()


class RegisterTestCase(TestCase):
  def setUp(self):
    self.data = {
      "email":"karan@email.com","password":"IamKaran","full_name":"karan maurya","phone":"9999999999","pincode":"666666"
    }
    self.invalid_data = {
      "password":"IamKaran","full_name":"karan maurya","phone":"9999999999","pincode":"666666"
    }
    self.client = APIClient()

  def test_valid_user_creation(self):
    response = self.client.post(reverse('register'),data=self.data,format="json")
    user = User.objects.get(email="karan@email.com")
    serializer = UserSerializer(user)
    self.assertEqual(response.data,serializer.data)
    self.assertEqual(response.status_code,status.HTTP_201_CREATED)

  def test_invalid_user_creation(self):
    response = self.client.post(reverse('register'),data=self.invalid_data,format="json")
    self.assertEqual(response.status_code,status.HTTP_400_BAD_REQUEST)
  