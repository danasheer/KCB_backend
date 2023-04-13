from rest_framework import serializers
from branches import models
from employees.serializers import EmployeeSerializer


class BrancheSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Branche
        fields = '__all__'


class FloorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Floor
        fields = '__all__'


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Department
        fields = '__all__'


class DepartmentDetailSerializer(serializers.ModelSerializer):
    employees = EmployeeSerializer(many=True)

    class Meta:
        model = models.Department
        fields = ['id', 'name', 'floor', 'employees']


class PrinterSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.printer
        fields = '__all__'
