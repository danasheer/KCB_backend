from rest_framework import serializers
from .models import Employee, Computer, Monitor, Scanner


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'


class ComputerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Computer
        fields = '__all__'


class MonitorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Monitor
        fields = '__all__'


class ScannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scanner
        fields = '__all__'


class EmployeeDetailSerializer(serializers.ModelSerializer):
    computers = ComputerSerializer(many=True)
    monitors = MonitorSerializer(many=True)
    scanners = ScannerSerializer(many=True)

    class Meta:
        model = Employee
        fields = ['id', 'name', 'position', 'department',
                  'computers', 'monitors', 'scanners']
