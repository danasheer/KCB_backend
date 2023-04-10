from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, RetrieveAPIView, UpdateAPIView
from branches import models
from .serializer import BrancheSerializer, FloorSerializer, PrinterSerializer, DepartmentSerializer
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
    permission_classes = [AllowAny]


class BrancheDeleteView(DestroyAPIView):
    queryset = models.Branche.objects.all()
    serializer_class = BrancheSerializer
    lookup_field = 'id'
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
    permission_classes = [AllowAny]


class FloorDeleteView(DestroyAPIView):
    queryset = models.Floor.objects.all()
    serializer_class = FloorSerializer
    lookup_field = 'id'
    permission_classes = [AllowAny]


class DepartmentListView(ListAPIView):
    queryset = models.department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [AllowAny]


class DepartmentCreateView(CreateAPIView):
    queryset = models.department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class DepartmentUpdateView(UpdateAPIView):
    queryset = models.department.objects.all()
    serializer_class = DepartmentSerializer
    lookup_field = 'id'
    permission_classes = [AllowAny]


class DepartmentDeleteView(DestroyAPIView):
    queryset = models.department.objects.all()
    serializer_class = DepartmentSerializer
    lookup_field = 'id'
    permission_classes = [AllowAny]


class PrintersListView(ListAPIView):
    queryset = models.printer.objects.all()
    serializer_class = PrinterSerializer
    permission_classes = [AllowAny]


class PrintersCreateView(CreateAPIView):
    queryset = models.printer.objects.all()
    serializer_class = PrinterSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PrintersUpdateView(UpdateAPIView):
    queryset = models.printer.objects.all()
    serializer_class = PrinterSerializer
    lookup_field = 'id'
    permission_classes = [AllowAny]


class PrintersDeleteView(DestroyAPIView):
    queryset = models.printer.objects.all()
    serializer_class = PrinterSerializer
    lookup_field = 'id'
    permission_classes = [AllowAny]
