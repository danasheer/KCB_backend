from rest_framework import serializers
from branches import models


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
        model = models.department
        fields = '__all__'
