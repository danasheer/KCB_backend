from django.shortcuts import render
from django.views.generic import ListAPIView, CreateAPIView, DestroyAPIView, RetrieveAPIView, UpdateAPIView
from branches import models
from .serializer import BrancheSerializer
from django.contrib.auth import get_user_model
from users.permissions import IsAuthenticated, IsAdminUser, AllowAny, IsOwner
from rest_framework.response import Response
from rest_framework import status


class BrancheListView(ListAPIView):
    queryset = models.Branche.objects.all()
    serializer_class = BrancheSerializer
    permission_classes = [AllowAny]


class BrancheCreateView(CreateAPIView):
    queryset = models.Branche.objects.all()
    serializer_class = BrancheSerializer
    permission_classes = [AllowAny]