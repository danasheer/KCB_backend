from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView
from .serializers import EmployeeSerializer, ComputerSerializer, MonitorSerializer, ScannerSerializer
from employees import models


class EmployeeListView(ListAPIView):
    queryset = models.Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeCreateView(CreateAPIView):
    queryset = models.Employee.objects.all()
    serializer_class = EmployeeSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class EmployeeUpdateView(UpdateAPIView):
    queryset = models.Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'object_id'


class EmployeeDeleteView(DestroyAPIView):
    queryset = models.Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'object_id'


class ComputerListView(ListAPIView):
    queryset = models.Computer.objects.all()
    serializer_class = ComputerSerializer


class ComputerCreateView(CreateAPIView):
    queryset = models.Computer.objects.all()
    serializer_class = ComputerSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class ComputerUpdateView(UpdateAPIView):
    queryset = models.Computer.objects.all()
    serializer_class = ComputerSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'object_id'


class ComputerDeleteView(DestroyAPIView):

    queryset = models.Computer.objects.all()
    serializer_class = ComputerSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'object_id'


class MonitorListView(ListAPIView):
    queryset = models.Monitor.objects.all()
    serializer_class = MonitorSerializer


class MonitorCreateView(CreateAPIView):
    queryset = models.Monitor.objects.all()
    serializer_class = MonitorSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class MonitorUpdateView(UpdateAPIView):
    queryset = models.Monitor.objects.all()
    serializer_class = MonitorSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'object_id'


class MonitorDeleteView(DestroyAPIView):
    queryset = models.Monitor.objects.all()
    serializer_class = MonitorSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'object_id'


class ScannerListView(ListAPIView):
    queryset = models.Scanner.objects.all()
    serializer_class = ScannerSerializer


class ScannerCreateView(CreateAPIView):
    queryset = models.Scanner.objects.all()
    serializer_class = ScannerSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class ScannerUpdateView(UpdateAPIView):
    queryset = models.Scanner.objects.all()
    serializer_class = ScannerSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'object_id'


class ScannerDeleteView(DestroyAPIView):
    queryset = models.Scanner.objects.all()
    serializer_class = ScannerSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'object_id'
