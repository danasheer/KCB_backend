from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView
from .serializers import EmployeeSerializer
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
