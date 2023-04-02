from django.shortcuts import render
from django.views.generic import ListAPIView, CreateAPIView, DestroyAPIView, RetrieveAPIView, UpdateAPIView
from branches import models
from .serializer import BrancheSerializer, FloorSerializer
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

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class BrancheUpdateView(UpdateAPIView):
    queryset = models.Branche.objects.all()
    serializer_class = BrancheSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'object_id'
    permission_classes = [AllowAny]


class BrancheDeleteView(DestroyAPIView):
    queryset = models.Branche.objects.all()
    serializer_class = BrancheSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'object_id'
    permission_classes = [AllowAny]


class FloorListView(ListAPIView):
    queryset = models.Floor.objects.all()
    serializer_class = FloorSerializer
    permission_classes = [AllowAny]


class FloorCreateView(CreateAPIView):
    queryset = models.Floor.objects.all()
    serializer_class = FloorSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class FloorUpdateView(UpdateAPIView):
    queryset = models.Floor.objects.all()
    serializer_class = FloorSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'object_id'
    permission_classes = [AllowAny]


class FloorDeleteView(DestroyAPIView):
    queryset = models.Floor.objects.all()
    serializer_class = FloorSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'object_id'
    permission_classes = [AllowAny]
