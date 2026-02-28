from django.shortcuts import render
from rest_framework import generics
from django.contrib.auth.models import User
from .serializer import UserProfileSerializer
from rest_framework.permissions import IsAuthenticated

class UserList(generics.ListAPIView):
    queryset = User.objects.all()

    serializer_class = UserProfileSerializer

    permission_class = [IsAuthenticated]

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()

    serializer_class =  UserProfileSerializer

    permission_class = [IsAuthenticated]

# Create your views here.
