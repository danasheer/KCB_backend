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


class BrancheDetailSerializer(serializers.ModelSerializer):
    departments = serializers.SerializerMethodField('get_all_departments')

    def get_all_departments(self, obj):
        departments = []
        for floor in obj.floors.all():
            # floor.departments.all()
            departments.extend(floor.departments.all())
        print(departments)
        # return departments
        # print(obj.floors.all())
        # departments = obj.floor
        # serializer = DepartmentSerializer(departments, many=True)
        # return serializer.data
        return DepartmentSerializer(departments, many=True).data
        # return ""

    class Meta:
        model = models.Branche
        fields = ['id', 'name',  'departments']


class DepartmentDetailSerializer(serializers.ModelSerializer):
    employees = EmployeeSerializer(many=True)

    class Meta:
        model = models.Department
        fields = ['id', 'name', 'floor', 'employees']


class PrinterSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.printer
        fields = '__all__'
